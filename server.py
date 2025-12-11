from flask import Flask, redirect, request, render_template, url_for, make_response, session
from authlib.integrations.flask_client import OAuth
import datetime
import config
import uuid
from serverClasses.pokerGame import *
app = Flask(__name__)
app.secret_key = 'temporary'
oauth = OAuth(app)


sessions = {}
games = {}



CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
google = oauth.register(
    name = 'google',
    client_id = config.CLIENT_ID,
    client_secret = config.CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)


def get_current_user():
    session_token = request.cookies.get('session_token')
    if not session_token:
        return None
    user = sessions.get(session_token)
    if not user:
        return None
    if datetime.datetime.now() > user.get("expiration", datetime.datetime.min):
        return None
    return user

#I want login to be the default route
@app.route('/')
def entryPage():
    return redirect('/login')

@app.route('/login')
def loginPage():
    user = get_current_user()
    if user:
        return redirect('/dashboard')
    
    return render_template('./loginPage.html')


@app.route('/dashboard')
def homePage():
    user = get_current_user()
    if not user:
        return redirect('/login')
    return "Dashboard Page Placeholder"


@app.route('/start-google-login')
def start_google_login(): 
    return google.authorize_redirect(url_for('authorize', _external=True), prompt='select_account')

@app.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    sessionCookie = str(uuid.uuid4())
    
    if token['userinfo']['email_verified'] == False:
         return "Email not Verified"
    
    
    sessions[sessionCookie] = token['userinfo']
    response = make_response(redirect('/dashboard'))
    expirationTime = datetime.datetime.now() + datetime.timedelta(seconds=3600)
    sessions[sessionCookie]["expiration"] = expirationTime
    response.set_cookie("session_token", sessionCookie, httponly=True)
    #print(f'Token UUID: {sessionToken} \nSessionToken: {sessions[sessionToken]}')
    print(sessions)

    return response

@app.route('/poker')
def pokerGame():
    #If not valid session token, redirect to login
    user = get_current_user()
    if not user:
        return redirect('/login')
    
    game_id = request.args.get('gameId')

    if not game_id or (game_id not in games):
        game = PokerGame()
        games[game.gameID] = game
        return redirect(f'/poker?gameId={game.gameID}')
    else:
        game = games.get(game_id)
    
    return "Poker Game Placeholder"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, request, render_template, url_for
from authlib.integrations.flask_client import OAuth

import config



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

#I want login to be the default route
@app.route('/')
def entryPage():
    return redirect('/login')

@app.route('/login')
def loginPage():
    #Need to check for session cookie
    #If valid session cookie, redirect to dashboard
    #Otherwise, stay
    
    return render_template('./loginPage.html')


@app.route('/dashboard')
def homePage():
    #If not valid session cookie, redirect to login
    return "Dashboard Page Placeholder"


@app.route('/start-google-login')
def start_google_login():
    return google.authorize_redirect(url_for('authorize', _external=True), prompt='select_account')

@app.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    print(token)
    return redirect('/dashboard')

@app.route('/poker')
def pokerGame():
    #If not valid session token, redirect to login


    game_id = request.args.get('gameId')

    #if gameid none, create new game
    return "Poker Game Placeholder"

if __name__ == "__main__":
    app.run(debug=True)
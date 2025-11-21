from flask import Flask, redirect, request

app = Flask(__name__)

sessions = {}
games = {}

@app.route('/')
def entryPage():
    return redirect('/login')

@app.route('/login')
def loginPage():
    #Need to check for session cookie
    #If valid session cookie, redirect to dashboard
    #Otherwise, stay
    
    return "Login Page Placeholder"


@app.route('/dashboard')
def homePage():
    #If not valid session cookie, redirect to login
    return "Dashboard Page Placeholder"


@app.route('/poker')
def pokerGame():
    #If not valid session token, redirect to login


    game_id = request.args.get('gameId')

    #if gameid none, create new game
    return "Poker Game Placeholder"

if __name__ == "__main__":
    app.run(debug=True)
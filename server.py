"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'bad', 'not good', 'no', 'uh oh', 'oh no', 'awful', 'terrible', 'nope']


@app.route('/')
def start_here():
  
    """Home page."""

    return "<!doctype html> <html><a href='/hello'>Hi! This is the home page.</a></html>"

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          what compliment would you like?<br>
          <input type="radio" name="insults" id="bad" value="bad">Bad <br>
          <input type="radio" name="insults" id="awful" value="awful">Awful <br>
          <input type="radio" name="insults" id="no" value="no">No<br>
          <input type="radio" name="insults" id="oh-no" value="oh-no">Oh-no <br>
          <input type="radio" name="insults" id="not good" value="not good">Not good<br>
          <input type="radio" name="insults" id="terrible" value= "terrible" >Terrible<br>
          <input type="radio" name="insults" id="nope" value="nope">Nope <br>
          <input type="radio" name="insults" id="uh oh" value="uh oh">Uh oh<br
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          what compliment would you like?<br>
          <input type="radio" name="compliments" id="awesome" value="awesome">Awesome <br>
          <input type="radio" name="compliments" id="terrific" value="terrific">Terrifc <br>
          <input type="radio" name="compliments" id="fantastic" value="fantastic">Fantastic <br>
          <input type="radio" name="compliments" id="fantabulous" value="fantabulous">Fantabulous <br>
          <input type="radio" name="compliments" id="neato" value="great_job">Great Job <br>
          <input type="radio" name="compliments" id="wowza" value= "wowza" >Wowza <br>
          <input type="radio" name="compliments" id="oh-so-not-meh" value="oh-so-not-meh">Oh-so-not-meh <br>
          <input type="radio" name="compliments" id="brilliant" value="brilliant">Brilliant <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    insult = request.args.get("insults")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('five_game.html')

@app.route('/login')
def login():
	return render_template('login.html')

app.run(host='0.0.0.0')
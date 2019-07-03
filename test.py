from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return redirect('five_game.html')
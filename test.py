from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return redirect('/login')

@app.route('/login')
def login():
	return render_template('login.html')

app.run(host='0.0.0.0')

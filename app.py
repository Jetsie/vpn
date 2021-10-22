from typing import Match
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")

@app.route("/api")
def api():
	return get(f'https://google.com/').content
	# url = request.args.get('url')
	# flash(url)
	# if request.method == 'GET':
    # 	user = request.form['nm']
    # 	return redirect(url_for('success',name = user))
	# elif request.method == 'HEAD':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'POST':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'PUT':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'DELETE':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'CONNECT':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'OPTIONS':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'TRACE':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	# elif request.method == 'PATCH':
	# 	user = request.form['nm']
	# 	return redirect(url_for('success',name = user))
	
	
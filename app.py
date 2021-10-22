from typing import Match
from flask import Flask, render_template, request, flash, Response
import requests
import urllib

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
	url = request.args.get('url')
	headers = dict(request.headers)
	# Edit Host header
	if headers['Host']:
		headers['Host'] = urllib.parse.urlparse(url).netloc

	if request.method == 'GET':
		print(headers)
		# Get third party page
		tpr = requests.get(url, headers=headers)
		# Clone tpr response to our response
		print(tpr.headers)
		resp = Response(tpr.content)
		resp.headers = tpr.headers
		return resp
	elif request.method == 'HEAD':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'PUT':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'DELETE':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'CONNECT':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'OPTIONS':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'TRACE':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	elif request.method == 'PATCH':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	
	
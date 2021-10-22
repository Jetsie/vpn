from typing import Match
from flask import Flask, render_template, request, flash, make_response
import requests
import urllib
from bs4 import BeautifulSoup

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

def find_list_resources (tag, attribute,soup, url):
	for x in soup.findAll(tag):
		try:
			x[attribute] = urllib.urljoin(url, x[attribute])
		except KeyError:
			pass
	return soup

# soup = BeautifulSoup(html)

# image_scr = find_list_resources('img',"src",soup)   
# scipt_src = find_list_resources('script',"src",soup)    
# css_link = find_list_resources("link","href",soup)
# video_src = find_list_resources("video","src",soup)         
# audio_src = find_list_resources("audio","src",soup) 
# iframe_src = find_list_resources("iframe","src",soup)
# embed_src = find_list_resources("embed","src",soup)
# object_data = find_list_resources("object","data",soup)         
# soruce_src = find_list_resources("source","src",soup)    


@app.route("/api")
def api():
	url = request.args.get('url')
	headers = dict(request.headers)
	# Edit Host header
	if headers['Host']:
		headers['Host'] = urllib.parse.urlparse(url).netloc

	if request.method == 'GET':
		tpr = requests.get(url, headers=headers)

		modded = find_list_resources('img',"src",BeautifulSoup(tpr.content), urllib.parse.urlparse(url).netloc)  
		return make_response((modded, tpr.status_code, dict(tpr.headers)))
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
	
	
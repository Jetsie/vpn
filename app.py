from typing import Match
from flask import Flask, render_template, request, flash, make_response
import requests
import urllib.parse as urllib
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

def urlToApi(url, base):
    if bool(urlparse(url).netloc):
        return f'https://radford.herokuapp.com/api?url={url}'
    elif url.startswith('{{') and url.endswith('}}'):
        return url
    else:
        return f'https://radford.herokuapp.com/api?url={urljoin(base, url)}'

def find_list_resources (tag, attribute, soup, domain):
   for x in soup.findAll(tag):
       try:
           x[attribute] = urlToApi(x[attribute], domain)
       except KeyError:
           pass
   return(soup)

def proxyHTML(html, domain):
    soup = BeautifulSoup(html, features="html.parser")

    soup = find_list_resources('img', "src", soup, domain)
    soup = find_list_resources('script', "src", soup, domain)
    soup = find_list_resources("link", "href", soup, domain)
    soup = find_list_resources("video", "src", soup, domain)
    soup = find_list_resources("audio", "src", soup, domain)
    soup = find_list_resources("iframe", "src", soup, domain)
    soup = find_list_resources("embed", "src", soup, domain)
    soup = find_list_resources("object", "data", soup, domain)
    soup = find_list_resources("source", "src", soup, domain)

    return soup

@app.route("/api")
def api():
	url = request.args.get('url')
	headers = dict(request.headers)
	# Edit Host header
	if headers['Host']:
		headers['Host'] = urllib.urlparse(url).netloc

	if request.method == 'GET':
		tpr = requests.get(url, headers=headers)
		content = proxyHTML(tpr.content, urllib.urlparse(url).netloc)
		print(headers)
		
		return make_response((tpr.content, tpr.status_code, dict(tpr.headers)))
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
	
	
from typing import Match
from flask import Flask, render_template, request, flash, make_response, abort
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

def urlToApi(url, base, scheme):
    if bool(urllib.urlparse(url).netloc):
        return f'https://radford.herokuapp.com/api?url={url}'
    elif url.startswith('{{') and url.endswith('}}'):
        return url
    elif url.startswith('data:'):
        return url
    else:
        link = '/' if not url.startswith('/') else ''
        return f'https://radford.herokuapp.com/api?url={scheme}://{base}{link}{url}'
        

def find_list_resources (tag, attribute, soup, domain, scheme):
   for x in soup.findAll(tag):
       try:
           x[attribute] = urlToApi(x[attribute], domain, scheme)
       except KeyError:
           pass
   return(soup)

def proxyHTML(html, domain, scheme):
    soup = BeautifulSoup(html, features="html.parser")

    soup = find_list_resources('img', "src", soup, domain, scheme)
    soup = find_list_resources('script', "src", soup, domain, scheme)
    soup = find_list_resources("link", "href", soup, domain, scheme)
    soup = find_list_resources("video", "src", soup, domain, scheme)
    soup = find_list_resources("audio", "src", soup, domain, scheme)
    soup = find_list_resources("iframe", "src", soup, domain, scheme)
    soup = find_list_resources("embed", "src", soup, domain, scheme)
    soup = find_list_resources("object", "data", soup, domain, scheme)
    soup = find_list_resources("source", "src", soup, domain, scheme)

    return str(soup)

@app.route("/api")
def api():
    url = request.args.get('url')
    urlparse = urllib.urlparse(url)
    headers = dict(request.headers)
    # Edit Host header
    if headers['Host']:
        headers['Host'] = urlparse.netloc

    if request.method == 'GET':
        try:
            tpr = requests.get(url, headers=headers)
        except:
            abort(404)
        # encodings = dict(tpr.headers)['Content-Encoding'].strip(' ').split(',')
        # print(tpr.content)
        content = proxyHTML(tpr.content, urlparse.netloc, urlparse.scheme)
        response = make_response((content, tpr.status_code))
        return response
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
    
    
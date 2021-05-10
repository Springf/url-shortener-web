from flask import Flask,redirect
import sqlite3
from flask import render_template
from flask import request
from core.api import Shortener
from core.shortener import hash_shortener
from store.sqlite_store import SqliteStore
from core.validator import regex_validator

app = Flask(__name__)

host = 'http://localhost:5000/'

@app.route('/create', methods=['POST'])
def create():
    data = request.form
    s = Shortener(hash_shortener.shorten, SqliteStore(sqlite3.connect('url-store.db')), regex_validator.validate)
    try:
        return f"{host}{s.create(data['url'], data['user'])}"
    except ValueError as e:
        return str(e)

@app.route('/update', methods=['POST'])
def update():
    data = request.form
    print(data)
    s = Shortener(hash_shortener.shorten, SqliteStore(sqlite3.connect('url-store.db')), regex_validator.validate)
    try:
        short_url = data['short_url']
        url = data['url']
        if not short_url.lower().startswith('http://') or len(short_url) < len(host):
            return 'Invalid short URL'
        if short_url == url:
            return 'Cannot redirect to self.'
        short_url = short_url[-8:]
        print(short_url)
        if s.update(short_url, data['url'], data['user']):
            return 'URL updated successfully'
        return 'Cannot Update: either short URL does not exist or you are not the creator of the URL.'
    except ValueError as e:
        return str(e)

@app.route('/<shorturl>', methods=['GET'])
def retrieve(shorturl):
    s = Shortener(hash_shortener.shorten, SqliteStore(sqlite3.connect('url-store.db')), regex_validator.validate)
    try:
        return redirect(s.retrieve(shorturl))
    except ValueError as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config.js')
def config():
    return app.send_static_file('config.js')
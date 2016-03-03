#!/usr/bin/python3

from bottle import *

app = Bottle()

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file('style.css', root='/hometu/etudiants/l/e/E146294Q/Techprod/OpenData/rest/vue/')

@app.route('/ville')
def ville():
    return "coucou"

@app.route('/')
def hello():
     return static_file('index.html', root='')

run(app, host='localhost', port=8080)
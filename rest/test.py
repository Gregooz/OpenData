#!/usr/bin/python3
from bottle import *
from BD import *

app = Bottle()


@app.error(404)
def error404(error):
	return static_file('vue/404.html', root='')

@app.error(500)
def error500(error):
	return static_file('vue/404.html', root='')


@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/hometu/etudiants/l/e/E146294Q/Techprod/OpenData/rest/vue')

@app.route('/installation')
def installation():
	bd = BD()
	bd.connexion()
	return bd.getInstallation(request.GET.get('inst'))

@app.route('/ville')
def ville():
    bd = BD()
    bd.connexion()
    print(request.GET.get("recherche"))
    return bd.getInstallations(request.GET.get('recherche'))


@app.route('/')
def hello():
     return static_file('index.html', root='')

run(app, host='localhost', port=8080)
#!/usr/bin/python3
from bottle import *
from BD import *
from jsonData.JsonData import *

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
	return static_file('installation.html', root='vue/');

@app.route('/infos')
def getInfos():
    bd = BD()
    bd.connexion()
    return str(JsonData.getInfos(request.GET.get('inst'), bd.getCursor()))


@app.route('/getInstallations')
def getInstallation():
    bd = BD()
    bd.connexion()
    return str(JsonData.getInstallationVille(request.GET.get('ville'), request.GET.get('activite'), bd.getCursor()))

@app.route('/getInstallation')
def getInstallation():
    bd = BD()
    bd.connexion()
    return JsonData.getInstallation(request.GET.get('inst'), bd.getCursor())

@app.route('/ville')
def ville():
    bd = BD()
    bd.connexion()
    return static_file('installations.html', root='vue/')

@app.route('/carte')
def carte():
    return static_file('carte.html', root='vue/')


@app.route('/')
def hello():
     return static_file('index.html', root='')

run(app, host='0.0.0.0', port=8080)
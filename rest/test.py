#!/usr/bin/python3
from bottle import *
from BD import *
from jsonData.JsonData import *

app = Bottle()




#Route qui revoie sur la page d'accueil : index.html
@app.route('/')
def hello():
     return static_file('index.html', root='')

#Gestion des erreurs (404), renvoie vers une page spécifique
@app.error(404)
def error404(error):
	return static_file('vue/404.html', root='')

#Gestion des erreurs (500), renvoie vers une page spécifique
@app.error(500)
def error500(error):
	return static_file('vue/404.html', root='')

#Une route simple utilisé par exemple pour l'ajout de lien (Javascript, css) dan sle fichier HTML
@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/hometu/etudiants/l/e/E146294Q/Techprod/OpenData/rest/vue')

#Définition de la route /installation
#On fait afficher la page installation.html du dossier /vue
#Corespond à l'affichage d'une installation particulière
@app.route('/installation')
def installation():
	bd = BD()
	bd.connexion()
	return static_file('installation.html', root='vue/');

#Cette route est utilisé pour faire des requêtes JSON
#Ici pour avoir des infos sur une installation particulière
#Nécéssite des paramètres fourni en paramètres de l'URL
#@param : id_installation : l'id de l'installation 
@app.route('/infos')
def getInfos():
    bd = BD()
    bd.connexion()
    return str(JsonData.getInfos(request.GET.get('inst'), bd.getCursor()))


#Cette route est utilisé pour faire des requêtes JSON
#Ici pour avoir uns liste d'installations
#Nécéssite des paramètres fourni en paramètres de l'URL
#@param : ville : la ville recherché / activité : le type d'activité souhaité
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

#Définition de la route /installations
#On fait afficher la page installations.html du dossier /vue
#Corespond à l'affichage d'une liste d'installations
@app.route('/ville')
def ville():
    bd = BD()
    bd.connexion()
    return static_file('installations.html', root='vue/')




#On lance l'application
run(app, host='0.0.0.0', port=8080)
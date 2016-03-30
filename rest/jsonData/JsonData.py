import json


class JsonData:

	#####
	# Cette fonction renvoie au format JSON une liste d'installations en fonction des paramètres donnée
	# Un seul paramètre est suffisant pour utiliser cette fonction
	# @Param : activité : le nom de l'activité / ville : le nom de la ville / cursor : l'accès pour lire de la base de données 
	# @return : JSON Object
	#####
	def getInstallationVille(ville, activite, cursor):
		if(ville == "" and activite != ""):
			cursor.execute("select * from installation where id IN (select id_installation from equipement where id IN (select id_equipement from equipement_activite where id_activite IN (select id from activite where nom LIKE '%"+activite+"%')))")
		elif(ville != "" and activite == ""):
			cursor.execute("select * from installation where ville LIKE '%"+ville+"%' ")
		elif(ville != "" and activite != ""):
			cursor.execute("select * from installation where ville LIKE '%"+ville+"%' and id IN (select id_installation from equipement where id IN (select id_equipement from equipement_activite where id_activite IN (select id from activite where nom LIKE '%"+activite+"%')))")
		else:
			cursor.execute("select * from installation LIMIT 10")
		return json.dumps(cursor.fetchall())
	
	#####
	# Cette fonction permet de renvoyer au format JSON les éléments concernant une installation
	# @Param : id_installation : l'id de l'installation souhaité
	# @return : JSON Object
	#####
	def getInstallation(id_installation, cursor):
		cursor.execute("select * from installation where id = "+id_installation+"")
		return json.dumps(cursor.fetchone())
	
	#####
	# Cette fonction permet de renvoyer au format JSON les éléments concernant une installation et ces activités liés a celle-ci
	# @Param : id-installation : l'id de l'installation en question 
	# @return : JSON Object
	#####
	def getInfos(id_installation, cursor):
		cursor.execute("select nom from activite where id IN (select id_activite from equipement_activite WHERE id_equipement = (select id from equipement where id_installation="+id_installation+"))")
		return json.dumps(cursor.fetchall())

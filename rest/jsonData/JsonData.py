import json


class JsonData:


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

	def getInstallation(id_installation, cursor):
		cursor.execute("select * from installation where id = "+id_installation+"")
		return json.dumps(cursor.fetchone())

	def getInfos(id_installation, cursor):
		cursor.execute("select nom from activite where id IN (select id_activite from equipement_activite WHERE id_equipement = (select id from equipement where id_installation="+id_installation+"))")
		return json.dumps(cursor.fetchall())

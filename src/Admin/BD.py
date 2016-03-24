from mysql.connector import (connection)
from mysql.connector import errorcode
import csv
from Admin.DataBaseAdmin import *

class BD:

	cxn = None
	cursor = None

	########################################################
	##         Connexion à la base de données             ##
	########################################################
	def connexion(self):
		self.cnx = connection.MySQLConnection(user='E146294Q', password='E146294Q', host='infoweb', database='E146294Q')
		self.cursor = self.cnx.cursor()


	########################################################
	##         Insertion des données Installation         ##
	########################################################	
	def insertionDonneesInstallation(self):
		cr = csv.reader(open("../data/installations.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if (compteur != 0):
				tmp = row[0].replace("'", "''")
				if(row[4] == ""):
					row[4]="00000"
				self.cursor.execute("INSERT INTO `installation` VALUES ("+row[1]+", '"+tmp+"', '"+row[7].replace("'", "''")+"', "+row[4]+", '"+row[2].replace("'", "''")+"', "+row[9]+", "+row[10]+")" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	########################################################
	##         Insertion des données Equipement           ##
	########################################################
	def insertionDonneesEquipenement(self):
		cr = csv.reader(open("../data/equipements.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if (compteur != 0 and self.verifierEquipement(row[2]) ):
				self.cursor.execute("INSERT INTO `equipement` VALUES ("+row[4]+", '"+row[3].replace("'", " ")+"', "+row[2]+")" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	def verifierEquipement(self, id_equipement):
		self.cursor.execute("select * from equipement where id_installation = "+id_equipement+"")
		if(len(self.cursor.fetchall()) == 0):
			return True
		else:
			return False

	########################################################
	##           Insertion des données Activité           ##
	########################################################
	def insertionDonneesActivite(self):
		cr = csv.reader(open("../data/activites.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if(row[4] == ""):
				row[4] = "0"
			if(row[5] == ""):
				row[5] = "none"
			if (compteur != 0 and self.verifierActivite(row[4])):
				self.cursor.execute("INSERT INTO `activite` VALUES ("+row[4]+", '"+row[5].replace("'", " ")+"' )" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	def verifierActivite(self, id_activite):
		print(id_activite)
		self.cursor.execute("select * from activite where id = "+id_activite+"")
		if(len(self.cursor.fetchall()) == 0):
			return True
		else:
			return False


	########################################################
	##       Ajout dans la table Activité-Equipement      ##
	########################################################
	def insertionDonneesActiviteEquipement(self):
		cr = csv.reader(open("../data/activites.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if(row[4] == ""):
				row[4] = "0";
			if (compteur != 0 and self.verifierEquipementBis(row[2], row[4]) ):
				self.cursor.execute("INSERT INTO `equipement_activite` VALUES ("+row[2]+", "+row[4]+" )" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	def verifierEquipementBis(self, id_equipement, id_activite):
		self.cursor.execute("select * from equipement_activite where id_equipement = "+id_equipement+" and id_activite = "+id_activite+"")
		if(len(self.cursor.fetchall()) == 0):
			return True
		else:
			return False


	########################################################
	##                Déconnexion de la base              ##
	########################################################
	def deconnexion(self):
		self.cnx.close()




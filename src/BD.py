from mysql.connector import (connection)
from mysql.connector import errorcode
import csv

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
	##         Création de la table installation         ##
	########################################################
	def creationTables(self):
		TABLES = {}
		TABLES['installation'] = (
    	"CREATE TABLE `installation` ("
    	"	`id` int(10) NOT NULL,"
    	"   `nom` varchar(255) NOT NULL,"
    	"   `adresse` varchar(255),"
    	"   `code_postal` int(5),"
    	"   `ville` varchar(255) NOT NULL,"
    	"   `latitude` float(25) NOT NULL,"
    	"   `longitude` float(25) NOT NULL,"
    	"   PRIMARY KEY (`id`)"
    	") ")

		########################################################
		##         Création de la table équipements          ##
		########################################################

		TABLES['equipement'] = (
    	"CREATE TABLE `equipement` ("
    	"	`id` int(10) NOT NULL,"
    	"   `nom` varchar(255) NOT NULL,"
	    "   `id_installation` int(10) NOT NULL,"
	    "   PRIMARY KEY (`id`),"
	    "   CONSTRAINT `fk_installation` FOREIGN KEY (`id_installation`)"
	    "		REFERENCES `installation` (`id`) ON DELETE CASCADE"
	    ") ")
		########################################################
		##         Création de la table activités             ##
		########################################################

		TABLES['activite'] = (
		    "CREATE TABLE `activite` ("
		    "  `id` int(10) NOT NULL,"
		    "  `nom` varchar(255) NOT NULL,"
		    "	KEY (`id`)"
		    ") ")

		########################################################
		##       Création de la table equipement_activite    ##
		########################################################		
		TABLES['equipement_activite'] = (
			"CREATE TABLE `equipement_activite` ("
			"  `id_equipement` int(10) NOT NULL,"
			"  `id_activite` int(10) NOT NULL,"
			"	KEY `id_equipement` (`id_equipement`),"
			"	KEY `id_activite` (`id_activite`),"
			"	CONSTRAINT `fk_equipement` FOREIGN KEY (`id_equipement`)"
			"		REFERENCES `equipement` (`id`) ON DELETE CASCADE,"
			"	CONSTRAINT `fk_activite` FOREIGN KEY (`id_activite`)"
			"		REFERENCES `activite` (`id`) ON DELETE CASCADE"
			") ")

		self.cursor.execute(TABLES['installation'])
		self.cursor.execute(TABLES['equipement'])
		self.cursor.execute(TABLES['activite'])
		self.cursor.execute(TABLES['equipement_activite'])
		# try:
		# except:
		# 	print("Les Tables sont déja crée")

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
			if (compteur != 0):
				self.cursor.execute("INSERT INTO `equipement` VALUES ("+row[4]+", '"+row[3].replace("'", " ")+"', "+row[2]+")" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	########################################################
	##           Insertion des données Activité           ##
	########################################################
	def insertionDonneesActivite(self):
		cr = csv.reader(open("../data/activites.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if (compteur != 0):
				if(row[4] == ""):
					row[4] = "0"
				if(row[5] == ""):
					row[5] = "none"
				self.cursor.execute("INSERT INTO `activite` VALUES ("+row[4]+", '"+row[5].replace("'", " ")+"' )" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")

	########################################################
	##       Ajout dans la table Activité-Equipement      ##
	########################################################
	def insertionDonneesActiviteEquipement(self):
		cr = csv.reader(open("../data/activites.csv",  encoding='utf-8'))
		compteur = 0
		for row in cr:
			if (compteur != 0):
				if(row[4] == ""):
					row[4] = "0";
				self.cursor.execute("INSERT INTO `equipement_activite` VALUES ("+row[2]+", "+row[4]+" )" )
				self.cnx.commit()
				compteur = compteur +1
				print(compteur)
			else:
				compteur = compteur+1
		print("Fin")



	########################################################
	##                Déconnexion de la base              ##
	########################################################
	def deconnexion(self):
		self.cnx.close()




########################################################
##    Utilisation des méthodes pour créer la base	  ##
##			    et ajouter les données                ##
########################################################
bd = BD()
bd.connexion()
bd.creationTables()
bd.insertionDonneesInstallation()
bd.insertionDonneesEquipenement()
bd.insertionDonneesActivite()
bd.insertionDonneesActiviteEquipement()
bd.deconnexion()
########################################################


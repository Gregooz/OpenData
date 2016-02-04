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
    	"   `adresse` varchar(255) NOT NULL,"
    	"   `code_postal` int(5) NOT NULL,"
    	"   `ville` varchar(255) NOT NULL,"
    	"   `latitude` float(15) NOT NULL,"
    	"   `longitude` float(15) NOT NULL,"
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
		    "  PRIMARY KEY (`id`)"
		    ") ")

		########################################################
		##       Création de la table equipement_activite    ##
		########################################################		
		TABLES['equipement_activite'] = (
			"CREATE TABLE `equipement_activite` ("
			"  `id_equipement` int(10) NOT NULL,"
			"  `id_activite` int(10) NOT NULL,"
			"	PRIMARY KEY (`id_equipement`, `id_activite`),"
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

	
	def insertionDonnees(self):
		cr = csv.reader(open("../data/installations.csv"))
		compteur = 0
		for row in cr:
			if (compteur != 0):
				self.cursor.execute("INSERT INTO `installation` VALUES ("+row[1]+", '"+row[0].replace("'", " ")+"', '"+row[7].replace("'", " ")+"', "+row[4]+", '"+row[2].replace("'", " ")+"', "+row[9]+", "+row[10]+")" )
				self.cnx.commit()
				compteur = compteur +1
			else:
				compteur = compteur+1




	def deconnexion(self):
		self.cnx.close()


bd = BD()
bd.connexion()
bd.creationTables()
bd.insertionDonnees()
bd.deconnexion()



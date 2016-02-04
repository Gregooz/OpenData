from mysql.connector import (connection)
from mysql.connector import errorcode

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
	##         Création de la table installations         ##
	########################################################
	def creationTables(self):
		TABLES = {}
		TABLES['installations'] = (
    	"CREATE TABLE `installations` ("
    	"  `nom_installation` varchar(255) NOT NULL,"
    	"  `numero_installation` int(20) NOT NULL,"
    	"  `nom_commune` varchar(255) NOT NULL,"
    	"  `code_insee` int(10) NOT NULL,"
    	"  `date_maj` date NOT NULL,"
    	"  `longitude` float(15) NOT NULL,"
    	"  `latitude` float(15) NOT NULL,"
    	"  PRIMARY KEY (`code_insee`)"
    	") ")

		########################################################
		##         Création de la table équipements          ##
		########################################################

		TABLES['equipements'] = (
    	"CREATE TABLE `equipements` ("
    	"  `code_INSEE` int(10) NOT NULL,"
    	"  `nom_commune` varchar(255) NOT NULL,"
    	"  `nom_equipement` varchar(255) NOT NULL,"
	    "  `id_equipement` varchar(255) NOT NULL,"
	    "  PRIMARY KEY (`code_INSEE`)"
	    ") ")

		########################################################
		##         Création de la table activités             ##
		########################################################

		TABLES['activites'] = (
		    "CREATE TABLE `activites` ("
		    "  `code_INSEE` int(10) NOT NULL,"
		    "  `num_fiche_equipement` int(15) NOT NULL,"
		    "  `activite_libelle` varchar(255) NOT NULL,"
		    "  `nom_commune` varchar(255) NOT NULL,"
		    "  PRIMARY KEY (`code_INSEE`)"
		    ") ")


		try:
			self.cursor.execute(TABLES['equipements'])
			self.cursor.execute(TABLES['installations'])
			self.cursor.execute(TABLES['activites'])
		except:
			print("Les Tables sont déja crée")


	def deconnexion(self):
		self.cnx.close()


bd = BD()
bd.connexion()
bd.creationTables()
bd.deconnexion()



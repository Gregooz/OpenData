from mysql.connector import (connection)
from mysql.connector import errorcode

		########################################################
		##         Création de la table équipements          ##
		########################################################
def creationTableInstallation(cursor):
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
	cursor.execute(TABLES['installation'])

		########################################################
		##         Création de la table équipements          ##
		########################################################
def creationTableEquipement(cursor):
	TABLES = {}
	TABLES['equipement'] = (
    	"CREATE TABLE `equipement` ("
    	"	`id` int(10) NOT NULL,"
    	"   `nom` varchar(255) NOT NULL,"
	    "   `id_installation` int(10) NOT NULL,"
	    "   PRIMARY KEY (`id`),"
	    "   CONSTRAINT `fk_installation` FOREIGN KEY (`id_installation`)"
	    "		REFERENCES `installation` (`id`) ON DELETE CASCADE"
	    ") ")
	cursor.execute(TABLES['equipement'])

		########################################################
		##         Création de la table activités             ##
		########################################################
def creationTableActivite(cursor):
	TABLES = {}
	TABLES['activite'] = (
		    "CREATE TABLE `activite` ("
		    "  `id` int(10) NOT NULL,"
		    "  `nom` varchar(255) NOT NULL,"
		    "	KEY (`id`)"
		    ") ")
	cursor.execute(TABLES['activite'])

		########################################################
		##       Création de la table equipement_activite    ##
		########################################################
def creationTableEquipementActivite(cursor):	
	TABLES = {}
	TABLES['equipement_activite'] = (
			"CREATE TABLE `equipement_activite` ("
			"  `id_equipement` int(10) NOT NULL,"
			"  `id_activite` int(10) NOT NULL,"
			"	KEY `id_equipement` (`id_equipement`),"
			"	KEY `id_activite` (`id_activite`)"
			") ")
	cursor.execute(TABLES['equipement_activite'])
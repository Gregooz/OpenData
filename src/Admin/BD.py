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
		self.cursor = self.cnx.cursor() #On récupère le curseur


	########################################################
	##         Insertion des données Installation         ##
	########################################################

	#####
	# Fonction qui insère l'ensembles des éléments du fichier CSV installation dans la table installation de la base
	# @Param : None
	# @return : void
	#####
	def insertionDonneesInstallation(self):
		cr = csv.reader(open("../data/installations.csv",  encoding='utf-8')) #On ouvre le CSV installations 
		compteur = 0
		for row in cr: #Pour chauqe linge du fichier
			if (compteur != 0): #On passe la première ligne avec les en-têtes
				tmp = row[0].replace("'", "''") #On suprimme les quotes qui pause des problèmes dans l'insertion de la base
				if(row[4] == ""): #On s'assure qu'il y a un code postal, sinon on met 00000 pour éviter les erreurs dans l'insertion de la base
					row[4]="00000"
				#On ajoute dans la base une ligne : Id (Code INSEE), le nom de l'installation, l'adresse, le code postal, la ville, la longitude et la latitude  
				self.cursor.execute("INSERT INTO `installation` VALUES ("+row[1]+", '"+tmp+"', '"+row[7].replace("'", "''")+"', "+row[4]+", '"+row[2].replace("'", "''")+"', "+row[9]+", "+row[10]+")" )
				self.cnx.commit() #On commit notre insertion
				compteur = compteur +1
				print(compteur) # On affcihe le nombre de ligne inséré pour voir l'évolution
			else:
				compteur = compteur+1
		print("Fin")

	########################################################
	##         Insertion des données Equipement           ##
	########################################################

	#####
	# Fonction qui insère l'ensembles des éléments du fichier CSV equipement dans la table equipement de la base
	# @Param : None
	# @return : void
	#####
	def insertionDonneesEquipenement(self):
		cr = csv.reader(open("../data/equipements.csv",  encoding='utf-8')) #On ouvre le CSV Equipements
		compteur = 0
		for row in cr: #Pour chauqe ligne du fichier
			if (compteur != 0 and self.verifierEquipement(row[2]) ): # On vérifie que numero d'installation correspondant n'existe pas déja  
				#On ajoute une ligne à la base : Id de l'équipement, le nom et le Numéro d'installation 
				self.cursor.execute("INSERT INTO `equipement` VALUES ("+row[4]+", '"+row[3].replace("'", " ")+"', "+row[2]+")" )
				self.cnx.commit() #On commit notre insertion
				compteur = compteur +1
				print(compteur) # On affcihe le nombre de ligne inséré pour voir l'évolution
			else:
				compteur = compteur+1
		print("Fin")

	#####
	# Permet de vérifier si une installation est déjà référencé dans la table equipement
	# @Param : id_equipement : l'id de l'installation 
	# @return : True si l'installation n'existe pas / False si elle existe déjà dans la base
	#####
	def verifierEquipement(self, id_equipement):
		self.cursor.execute("select * from equipement where id_installation = "+id_equipement+"")
		if(len(self.cursor.fetchall()) == 0):
			return True
		else:
			return False

	########################################################
	##           Insertion des données Activité           ##
	########################################################
	
	#####
	# Fonction qui insère l'ensembles des éléments du fichier CSV activité dans la table activité de la base
	# @Param : None
	# @return : void
	#####
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


	#####
	# Permet de vérifier si une activité est déjà référencé dans la table activité
	# @Param : id_activité : l'id de l'activité 
	# @return : True si l'activité n'existe pas / False si elle existe déjà dans la base
	#####
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

	#####
	# Fonction qui insère des éléments du fichier CSV activité dans la table equipement_activité de la base
	# @Param : None
	# @return : void
	#####
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


	#####
	# Permet de vérifier si un couple id_activité & id_équipement sont déjà référencé dans la base
	# @Param : id_activité : l'id de l'activité / id_equipement : l'id de l'équipement 
	# @return : True si le couple n'existe pas / False si il existe déjà dans la base
	#####
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




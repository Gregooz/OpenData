from Admin.BD import * #Import la class BD



########################################################
##    Utilisation des méthodes pour créer la base	  ##
##			    et ajouter les données                ##
########################################################

#Connexion à la base de données
bd = BD() 		#On construit un objet BD 
bd.connexion()	#On fait la connexion avec la base de donnée

#Création des Tables
creationTableInstallation(bd.cursor) 		#Table Installation
creationTableEquipement(bd.cursor) 			#Table Equipement
creationTableActivite(bd.cursor) 			#Table Activité
creationTableEquipementActivite(bd.cursor) 	#Table EquipementActivité

#Insertions des données dans la base
bd.insertionDonneesInstallation() 		#Insertion des données Installation
bd.insertionDonneesEquipenement()		#Insertion des données Equipement
bd.insertionDonneesActivite()			#Insertion des données Activités
bd.insertionDonneesActiviteEquipement()	#Insertion des données Activités et équipement

#Déconnexion de la base 
bd.deconnexion() #Déconnexion de la base
########################################################

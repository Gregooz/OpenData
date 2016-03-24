from Admin.BD import *



########################################################
##    Utilisation des méthodes pour créer la base	  ##
##			    et ajouter les données                ##
########################################################

#Connexion à la base de données
bd = BD()
bd.connexion()

#Création des Tables
creationTableInstallation(bd.cursor)
creationTableEquipement(bd.cursor)
creationTableActivite(bd.cursor)
creationTableEquipementActivite(bd.cursor)

#Insertions des données dans la base
bd.insertionDonneesInstallation()
bd.insertionDonneesEquipenement()
bd.insertionDonneesActivite()
bd.insertionDonneesActiviteEquipement()

#Déconnexion de la base 
bd.deconnexion()
########################################################

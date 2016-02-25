<?php

require_once __DIR__.("/../bean/installation.php");

class dao{

	private $connexion;
	

    /**
    *Fonction qui permet de se connecter à la base de données MySQL
    *
    *@param None
    *@return None
    */
	function connexion(){
		try {
		$this->connexion = new PDO('mysql:host=infoweb;charset=UTF8;dbname=E146294Q','E146294Q','E146294Q');
		$this->connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
      } catch(PDOException $e) {
		throw new ConnexionException("Erreur de connection");
      }
	}

    /**
    *Fonction qui permet de récupérer un ensemble d'instalations présente
    *dans une ville donnée en paramètres
    *
    *@param String ville
    *@return Array<Installation>
    */
	function getInstallations($motcles){
		$this->connexion();
		$requete = "SELECT * FROM `installation` WHERE ville LIKE '%".$motcles."%' LIMIT 10";
		$resultat = $this->connexion->query($requete);
		return $resultat->fetchAll(PDO::FETCH_CLASS, "installation");
	}

	/**
    *Fonction qui permet de récupérer une installation avec son id
    *
    *@param String id
    *@return Installation
    */
	function getInstallation($id){
		$this->connexion();
		$requete = "SELECT * FROM `installation` WHERE id=".$id;
		$resultat = $this->connexion->query($requete);
		$resultat->setFetchMode(PDO::FETCH_CLASS, 'installation');
        return $resultat->fetch();
	}



    /**
    *Fonction qui permet de se déconnecter de la base de données MySQL
    *
    *@param None
    *@return None
    */
	function deconexion(){
		$this->connexion == null;
	}





}





?>
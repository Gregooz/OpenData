<?php

require_once __DIR__.("/../bean/installation.php");

class dao{

	private $connexion;
	
	function connexion(){
		try {
		$this->connexion = new PDO('mysql:host=localhost;charset=UTF8;dbname=prod','root','');
		$this->connexion->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
      } catch(PDOException $e) {
		throw new ConnexionException("Erreur de connection");
      }
	}


	function getInstallations($motcles){
		$this->connexion();
		$requete = "SELECT * FROM `installation` WHERE ville LIKE '%".$motcles."%' LIMIT 10";
		$resultat = $this->connexion->query($requete);
		return $resultat->fetchAll(PDO::FETCH_CLASS, "installation");
	}






	function deconexion(){
		$this->connexion == null;
	}





}





?>
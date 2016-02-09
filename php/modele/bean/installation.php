<?php

class installation {


	private $id;
	private $nom;
	private $adresse;
	private $code_postal;
	private $ville;
	private $latitude;
	private $longitude;


	function getId(){
		return $this->id;
	}

	function getNom(){
		return $this->nom;
	}
	
	function getAdresse(){
		return $this->adresse;
	}

	function getCodePostal(){
		return $this->code_postal;
	}

	function getVille(){
		return $this->ville;
	}

	function getLatitude(){
		return $this->latitude;
	}

	function getLongitude(){
		return $this->longitude;
	}







}




?>
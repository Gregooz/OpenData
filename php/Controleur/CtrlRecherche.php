<?php

require_once __DIR__.("/../modele/dao/dao.php");
require_once __DIR__.("/../modele/bean/installation.php");
require_once __DIR__.("/../vue/vueInstallation.php");

class CtrlRecherche{

	private $recherche;


	function __construct($recherche){
		$this->recherche = $recherche;
	}


	function demarrer(){
		$dao = new dao();
		$tab_installations = $dao->getInstallations($this->recherche);

		$html="";
		$vue = new vueInstallation();
		foreach ($tab_installations as $installation) {
			$html .= $vue->generer1Installation($installation);
		}

		$vue->afficher($html);


	}





}

















?>
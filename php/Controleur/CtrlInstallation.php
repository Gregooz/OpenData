<?php

require_once __DIR__.("/../modele/dao/dao.php");
require_once __DIR__.("/../modele/bean/installation.php");
require_once __DIR__.("/../vue/vueInstallation.php");

class CtrlInstallation{

	private $id;
	private $dao;
	private $vue;


	function __construct($id){
		$this->id = $id;
	}

	function demarrer(){
		$this->dao = new Dao();
		$installation = $this->dao->getInstallation($this->id);
		$this->vue = new vueInstallation();

		$html = $this->vue->generer1Installation($installation);
		$this->vue->afficher($html);


	}

}
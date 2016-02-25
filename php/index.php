<?php

require_once __DIR__.("/Controleur/CtrlRecherche.php");
require_once __DIR__.("/Controleur/CtrlInstallation.php");


if(isset($_GET['inst'])){
	$CtrlInst = new CtrlInstallation($_GET['inst']);
	$CtrlInst->demarrer();
}

if(isset($_GET['recherche'])){
	$CtrlRech = new CtrlRecherche($_GET['recherche']);
	$CtrlRech->demarrer();
}


else{
	include "static/acceuil.html";
}







?>

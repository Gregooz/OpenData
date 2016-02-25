<?php

require_once __DIR__.("/../vue/vueInstallation.php");
require_once __DIR__.("/../modele/bean/installation.php");

class vueInstallation{


	function generer1Installation($installation){
		return $htlm = "<title>Installations de ".$installation->getVille()."</title>
						<div class=login> <div class=login-screen>
						<div class=app-title>
						<h1 style=font-size:50px>".$installation->getNom()."</h1>
						</div>
						<table><td class=texte>
						<div class=nom data-value=".$installation->getVille().">Nom : ".$installation->getNom()."</div>
						Adresse : ".$installation->getAdresse()."
						<div class=latitude data-value=".$installation->getLatitude()."></div>
						<div class=longitude data-value=".$installation->getLongitude()."></div> <br><br>
						<form method='GET'>
						<input type=hidden name=inst value=".$installation->getId()." />
						<input type=submit class=btn btn-primary btn-large btn-block value='En Savoir plus...' />
						</form>
						</td><td>
						<div class=div_carte></div>
						</td></table>
						</div></div><br>";
	}


	function afficher($code_html){
		$html = "<html>".$this->genererEnTetes()."<body> <script type=text/javascript src=https://maps.googleapis.com/maps/api/js?v=3></script> ";
		$html .= $code_html;

		$html .= "<script type=text/javascript>
        			function initialize() {
  						elems = document.getElementsByClassName('div_carte');
  						latitudes = document.getElementsByClassName('latitude');
  						longitudes = document.getElementsByClassName('longitude');
  						villes = document.getElementsByClassName('nom');
  						for (var i = 0; i < elems.length; i++) {
  							var myLatlng = new google.maps.LatLng(longitudes[i].getAttribute('data-value'), latitudes[i].getAttribute('data-value'));
  							var mapOptions = { zoom: 15, center : myLatlng };
    						var map = new google.maps.Map(elems[i], mapOptions);

    						var marker = new google.maps.Marker({
    						position: myLatlng,
    						map: map,
    						title: villes[i].getAttribute('data-value')
  							});
  						}
					}
					google.maps.event.addDomListener(window, 'load', initialize);
    </script>";

    echo $html;

	}


	function genererEnTetes(){
		return "<link rel=stylesheet href=vue/style.css>
				<meta http-equiv=content-type content=text/html charset=utf-8 />";

	}

}



?>
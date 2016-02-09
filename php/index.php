<?php

require_once __DIR__.("/Controleur/CtrlRecherche.php");


if(isset($_GET['inst'])){
	echo 'coucou';
}

if(isset($_GET['recherche'])){
	$CtrlRech = new CtrlRecherche($_GET['recherche']);
	$CtrlRech->demarrer();
}


else{
	echo "<html><head><link rel=stylesheet href=vue/style.css></head><body>
		<div class=login> <div class=login-screen>
		<div class=app-title>
		<h1 style=font-size:50px>Faire une recherche</h1>
		</div>
		<div class=login-form >
		<form method=GET action= >
			<input type=text class=imput placeholder='Ex : Nantes' name=recherche /><br><br><br><br>
			<input class='btn2 btn-primary btn2-large btn2-block' type=submit value=Rechercher />
		</form>
		</div>

		</div></div>
		</body></html>";
}







?>

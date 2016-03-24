$(document).ready(function(){

$('#valider').click(function(){
	$.ajax({
		url:'localhost:8080/getInstallation',
		type:'GET',
		dataType:'json',
		jsonp: 'jsoncallback', // a renseigner d'après la doc du service, par défaut callback
		data:'ville=nantes',
		success:function(data){
			$("#test1").html('');
			$.each(data, function(i,item){
	            $("#test1").append("<div>"+item.nom+"</div>");
				if ( i == 20 ){
	            	return false ; 
	            }
	        });
	          },
	error: function(resultat,statut,erreur){
	alert("erreur");},
	 
	})

});

});
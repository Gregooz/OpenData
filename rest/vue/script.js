$(document).ready(function(){

$('#valider').click(function(){
	$.ajax({
		url:'http://localhost:8080/getInstallations',
		type:'GET',
		data:'ville=nantes',
		success:function(data){
			data = $.parseJSON(data);
			$("#test1").html('');
			$.each(data, function(i,item){
	            $("#test1").append("<div>"+item[0]+"</div>");
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
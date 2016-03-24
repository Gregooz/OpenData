function initialiser() {


var latlng = new google.maps.LatLng(46.779231, 6.659431);
				//objet contenant des propriétés avec des identificateurs prédéfinis dans Google Maps permettant
				//de définir des options d'affichage de notre carte
				var options = {
					center: latlng,
					zoom: 19,
					mapTypeId: google.maps.MapTypeId.ROADMAP
				};
				
				//constructeur de la carte qui prend en paramêtre le conteneur HTML
				//dans lequel la carte doit s'afficher et les options
				var map = new google.maps.Map(document.getElementById("carte"), options);
				var tMarker = [];

			   $.ajax({
			        url:'http://localhost:8080/getInstallations',
			        type:'GET',
			        data:'ville=&activite=',
			        success:function(data){
			            data = $.parseJSON(data);
			            $.each(data, function(i,item){
			     			tMarker.push({ lat : item[5], lon : item[6], title : item[1]});
			                }
			            );
				              },
				    error: function(resultat,statut,erreur){
				    alert("erreur");},
				    });


						for( i = 0; i < tMarker.length; i++){
						    data = tMarker[i];
						    oLatLng = new google.maps.LatLng( data.lat, data.lon);
						    oMarker = new google.maps.Marker({
						      position : oLatLng,
						      map : map,
						      title : data.title
						    });
						  }


				
}



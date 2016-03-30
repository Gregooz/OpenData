$( document ).ready(function() {

$.ajax({
        url:'http://localhost:8080/infos',
        type:'GET',
        data:'inst='+getParameter('inst'),
        success:function(data){
            data = $.parseJSON(data);
            $("#principal").html('');
            $.each(data, function(i,item){
              for(i=0;i<item.length;i++){
                $("#act").append(item[i] + "<br>");
              }
                if ( i == 10 ){
                return false ;
                }
            });
              },
    error: function(resultat,statut,erreur){
    alert("erreur");},
    });




$.ajax({
        url:'http://localhost:8080/getInstallation',
        type:'GET',
        data:'inst='+getParameter('inst'),
        success:function(data){
            data = $.parseJSON(data);
            $("#nom").append(data[1]);
            $("#rue").append(data[2]);
            $("#cp").append(data[3]);
            $("#ville").append(data[4]);
            initialize(data[5], data[6], data[1]);
              },
    error: function(resultat,statut,erreur){
    alert("erreur");},
    });




});



//Fonction qui initialise la google map pour bonne positions
//Longitude et latitude récupéré avec la requête JSON
function initialize(lon, lat, titre) {
  var myLatlng = new google.maps.LatLng(lat,lon);
    var mapOptions = { zoom: 18, 
            center : myLatlng,
            mapTypeId: google.maps.MapTypeId.HYBRID};
  
    var map = new google.maps.Map(document.getElementById('map'), mapOptions); // Initialise la google map dans le div "map" du modal
  //Place un marqueur sur la google map avec le titre de la photo
  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: titre
     });
}


function getParameter(theParameter) { 
  var params = window.location.search.substr(1).split('&');
 
  for (var i = 0; i < params.length; i++) {
    var p=params[i].split('=');
	if (p[0] == theParameter) {
	  return decodeURIComponent(p[1]);
	}
  }
  return false;
}
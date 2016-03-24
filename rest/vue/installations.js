$( document ).ready(function() {



console.log(decodeURI(getParameter('ville')));

    $.ajax({
        url:'http://localhost:8080/getInstallations',
        type:'GET',
        data:'ville='+getParameter('ville').replace("é", "e")+"&activite="+getParameter('activite'),
        success:function(data){
            data = $.parseJSON(data);
            $("#principal").html('');
            $.each(data, function(i,item){
                $("#principal").append(creation(item[1], item[2], item[5], item[6], item[0]));
                if ( i == 10 ){
                return false ;
                }
            });
              },
    error: function(resultat,statut,erreur){
    alert("erreur");},
    });

});


function creation(nom, addr, lat, longi, id)
{
    tmp = '<div class="container teal lighten-5" style="border-radius: 10px;"><div class="row"><div class="col s12 center grey-text text-darken-2"><h1>Title</h1>';
    tmp = tmp + '</div></div><div class="row grey-text text-darken-2"><div class="col s8"><div class="row"><div class="col s12 center nom" data-value='+nom+'><h5>Nom: '+nom+'</h5> </div></div>';
    tmp = tmp + '<div class="row"><div class="col s12 center"><h5>Adresse: '+addr+'</h5> </div></div><div class="latitude" data-value='+lat+' hidden></div>';
    tmp = tmp + '<div class="longitude" data-value='+longi+' hidden></div><div class="row"><form class="col s12" method=\'GET\' action=\'/installation\'> ';
    tmp = tmp + ' <input type="hidden" name="inst" value='+id+' /><div class="row center"><button class="btn-large waves-effect waves-light modal-trigger" type="submit" name="action" data-target="modal">En Savoir Plus...<i class="material-icons right">info_outline</i>';
    tmp = tmp + ' </button></div></form></div></div><div class="col s4"><div class="col s12 div_carte"></div> </div> </div>';
    return tmp;
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
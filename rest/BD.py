from mysql.connector import (connection)
from mysql.connector import errorcode

class BD:


	########################################################
	##         Connexion à la base de données             ##
	########################################################
	def connexion(self):
		self.cnx = connection.MySQLConnection(user='E146294Q', password='E146294Q', host='infoweb', database='E146294Q')
		self.cursor = self.cnx.cursor()
		return self.cnx


	def getInstallations(self, get_ville):
		html = ''' <html><meta charset='utf-8'><link rel=stylesheet href=/static/style.css>
				   <script type=text/javascript src=https://maps.googleapis.com/maps/api/js?v=3></script>
				   <script src=/static/w3-include-HTML.js></script>
				   <script type=text/javascript>
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
    			</script><body> <ul>
					  <li><a href="/">Home</a></li>
					  <li><a href="" class=active>News</a></li>
					  <li><a href="/">Contact</a></li>
					</ul>
 					'''


		self.cursor.execute("select * from installation where ville= '"+get_ville+"' LIMIT 10")
		for row in self.cursor.fetchall():
			tmp = "<div class=login> <div class=login-screen><div class=app-title>"
			tmp = tmp + "<h1 style=font-size:50px>" + str(row[1]) + "</h1></div>"
			tmp = tmp + "<table><td class=texte> <div class=nom data-value="+str(row[1])+">Nom : "+str(row[1])+"</div>"
			tmp = tmp + "Adresse : " + str(row[4])
			tmp = tmp + "<div class=latitude data-value="+str(row[5])+"></div>"
			tmp = tmp + "<div class=longitude data-value="+str(row[6])+"></div> <br><br>"
			tmp = tmp + ''' <form method='GET' action='/installation'>
						<input type=hidden name=inst value='''+str(row[0])+''' />
						<input type=submit class=btn btn-primary btn-large btn-block value='En Savoir plus...' />
						</form>
						</td><td>
						<div class=div_carte></div>
						</td></table>
						</div></div><br> '''
			html = html + tmp
		return html
						
	def getInstallation(self, id_installation):
		self.cursor.execute("select * from installation where id = "+id_installation+"")
		return str(self.cursor.fetchone())

						
	def getCursor(self):
		return self.cursor 				
						


	########################################################
	##      Deconnexion à la base de données              ##
	########################################################
	def deconnexion():
		self.cnx = None
import json
from BD import *


def test(ville):
	bd = BD()
	tmp = bd.connexion().cursor()
	tmp.execute("select * from installation where ville= '"+ville+"' LIMIT 10");

	rows = tmp.fetchall()
	 
	# Convert query to row arrays
	 
	rowarray_list = []
	for row in rows:
	    t = (row.ID, row.FirstName, row.LastName, row.Street, 
	         row.City, row.ST, row.Zip)
	    rowarray_list.append(t)
	 
	j = json.dumps(rowarray_list)
	rowarrays_file = 'student_rowarrays.js'
	f = open(rowarrays_file,'w')
	print >> f, j
	 
	# Convert query to objects of key-value pairs
	 
	objects_list = []
	for row in rows:
	    d = collections.OrderedDict()
	    d['id'] = row.ID
	    d['FirstName'] = row.FirstName
	    d['LastName'] = row.LastName
	    d['Street'] = row.Street
	    d['City'] = row.City
	    d['ST'] = row.ST
	    d['Zip'] = row.Zip
	    objects_list.append(d)
	 
	j = json.dumps(objects_list)
	objects_file = 'student_objects.js'
	f = open(objects_file,'w')
	print >> f, j


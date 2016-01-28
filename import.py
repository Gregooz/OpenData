import csv

cr = csv.reader(open("/hometu/etudiants/d/e/E146103H/INFO2/S4/ACDA/Tech Prod Log/TP/data/installations.csv","r"))
for row in cr:
    print (row)
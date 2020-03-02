import xmltodict

#Obtenemos el  archivo XML con open
stream = open('sample.xml', 'r')

#Parseamos la data
xml = xmltodict.parse(stream.read())

for e in xml['People']['Person']:
	print (F"hola {e['FirstName']} {e['LastName']} bienvenido al equipo de devnet")


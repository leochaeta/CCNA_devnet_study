import xmltodict

#Obtenemos el  archivo XML con open
stream = open('ejemplo.xml', 'r')

#Parseamos la data
xml = xmltodict.parse(stream.read())


print (xml)
print ("#" * 40)
for e in xml['People']['Person']:
	print (F"hola {e['FirstName']} {e['LastName']} bienvenido al equipo de devnet")


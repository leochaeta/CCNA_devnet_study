import yaml
from yaml import load, load_all

stream =open('ejemplo.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

#print (type(documents))

#A = list(documents)[0]['People']


#print (A[3])


#for z in documents:
#	print (z)

#for doc  in documents:
#	for x in range(0,3):
#		print (F"hola {doc['People'][x]['FirstName']} bienvenido al equipo de devnet")

#for doc in documents:
#	print (len(doc['People']))

#for doc in documents:
#	for x in range(0,len(doc['People'])):
#		print (F"hola {doc['People'][x]['FirstName']} bienvenido al equipo de devnet")


#for gen  in documents:
#	for x in gen["People"]:
#		if x['FirstName'] == "Eduardo":
#			print (x)

A = list(documents)[0]['People']
print (F"bienvenido {A[0]['FirstName']} {A[0]['LastName']}")


#Se transforma el generador a lista
#for doc  in list(documents)[0]['People']:
#	print (F"hola {doc['FirstName']} {doc['LastName']} bienvenido al equipo de devnet")
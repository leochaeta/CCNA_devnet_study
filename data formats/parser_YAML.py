import yaml
from yaml import load, load_all

stream =open('ejemplo.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

#print (type(documents))

for doc  in documents:
	for x in range(0,3):
		print (F"hola {doc['People'][x]['FirstName']} bienvenido al equipo de devnet")


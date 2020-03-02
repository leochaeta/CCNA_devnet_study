import json
jsonstr = """
{"People" :
   [
	{
		"Id": 1,
		"FirstName": "Juan",
		"LastName": "Perez",
		"Email": "juan.perez@ciberc.com"
	},
	{
		"Id": 2,
		"FirstName": "Raul",
		"LastName": "Flores",
		"Email": "raul.flores@ciberc.com"
	},
	{
		"Id": 3,
		"FirstName": "Eduardo",
		"LastName": "Najera",
		"Email": "eduardo.najera@ciberc.com"
	}
   ]
}
"""
print (type(jsonstr))

jsonobject =  json.loads(jsonstr)
print (type(jsonobject))
print (jsonobject)
print (jsonobject['People'][1]['Email'])

for x in jsonobject['People']:
	print (f"Bienvenido {x['FirstName']} {x['LastName']} al equipo")


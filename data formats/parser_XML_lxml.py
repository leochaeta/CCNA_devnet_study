from lxml import etree as ET

#obtener el archivo xml
stream = open('ejemplo.xml', 'r')

#Parsear la data en un objeto ElementTree 
xml = ET.parse(stream)

#obtener la etiqueta root (raiz del xml)
root = xml.getroot()

#Iterar en cada rama del elemento raiz
for e in root:
    #imprimir en formato string cada elemento
    print (ET.tostring(e))
    print ("")
    #imprimir el atributo ID de cada elemento
    print (e.get("Id"))


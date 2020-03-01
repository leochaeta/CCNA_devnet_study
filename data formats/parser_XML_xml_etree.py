import xml.etree.ElementTree as ET

#Get XML file
stream = open('sample.xml', 'r')

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the Root tag
root = xml.getroot()

#Iterate through each child of the root elment
for e in root:
    #Print the stringfied version of the element
    print (ET.tostring(e))
    print ("")
    #print the "ID" attribute of the element object
    print (e.get("Id"))


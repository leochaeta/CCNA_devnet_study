import xmltodict

#Get XML file
stream = open('sample.xml', 'r')

#Parse the data into an ElementTree object
xml = xmltodict.parse(stream.read())

for e in xml['People']['Person']:
	print (e)


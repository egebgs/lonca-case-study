from xml_parser import parse_xml

#Parsing the XML file
xml_file_path = '../data/lonca-sample.xml'
products_data = parse_xml(xml_file_path)

#Printing the parsed products
for product in products_data:
    print(product)

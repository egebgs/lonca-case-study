import xml.etree.ElementTree as ET


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    products = []

    for product_elem in root.findall('.//Product'):
        product_data = {
            'ProductId': product_elem.get('ProductId'),
            'Name': product_elem.get('Name'),
            'Images': [image_elem.get('Path') for image_elem in product_elem.findall('.//Image')],
            'ProductDetails': {detail_elem.get('Name'): detail_elem.get('Value') for detail_elem in
                               product_elem.findall('.//ProductDetail')},
            'Description': product_elem.find('.//Description').text.strip() if product_elem.find(
                './/Description') is not None else None
        }

        products.append(product_data)

    return products

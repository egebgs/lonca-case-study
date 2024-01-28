from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

def extract_description_info(description):
    soup = BeautifulSoup(description, 'html.parser')

    model_measurements_tag = soup.find('strong', text='Model Ölçüleri:')
    product_measurements_tag = soup.find('strong', text='Ürün Bilgisi:')
    fabric_tag = soup.find('strong', text='Kumaş Bilgisi:')

    model_measurements = model_measurements_tag.find_next('li').text.strip() if model_measurements_tag and model_measurements_tag.find_next('li') else ''
    product_measurements = product_measurements_tag.find_next('li').text.strip() if product_measurements_tag and product_measurements_tag.find_next('li') else ''
    fabric = fabric_tag.find_next('li').text.strip() if fabric_tag and fabric_tag.find_next('li') else ''

    return model_measurements, product_measurements, fabric

def transform_data(raw_data):
    transformed_data = []

    for product in raw_data:
        discounted_price = float(product['ProductDetails'].get('DiscountedPrice', 0).replace(',', '.'))
        price = float(product['ProductDetails'].get('Price', 0).replace(',', '.'))
        is_discounted = discounted_price != price and discounted_price != 0
        model_measurements, product_measurements, fabric = extract_description_info(product['Description'])

        transformed_product = {
            'ProductId': product['ProductId'],
            'Name': product['Name'].capitalize(),
            'Images': product['Images'],
            'Price': price,
            'DiscountedPrice': discounted_price,
            'ProductType': product['ProductDetails'].get('ProductType', ''),
            'Quantity': int(product['ProductDetails'].get('Quantity', 0)),
            'PriceUnit': product['ProductDetails'].get('PriceUnit', ''),
            'Color': product['ProductDetails'].get('Color', ''),
            'Fabric': fabric,  # Include the fabric value in the transformed product
            'Series': product['ProductDetails'].get('Series', ''),
            'SampleSize': product['ProductDetails'].get('SampleSize', ''),
            'ModelMeasurements': model_measurements,
            'ProductMeasurements': product_measurements,
            'Status': product['ProductDetails'].get('Status', ''),
            'IsDiscounted': is_discounted,
        }

        transformed_data.append(transformed_product)

    return transformed_data
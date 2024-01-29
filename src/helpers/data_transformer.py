from bs4 import BeautifulSoup


def extract_description_info(description):
    soup = BeautifulSoup(description, 'html.parser')

    # Find the tags
    model_measurements_tag = soup.find('strong', string=lambda text: 'Model Ölçüleri' in text)
    product_info_tag = soup.find('strong', string=lambda text: 'Ürün Ölçüleri' in text)
    fabric_info_tag = soup.find('strong', string=lambda text: 'Kumaş Bilgisi' in text)
    sample_size_tag = soup.find(string=lambda text: 'Modelin üzerindeki ürün' in text)

    # Extract the text
    model_measurements = model_measurements_tag.find_next_sibling(text=True).strip() if model_measurements_tag and model_measurements_tag.find_next_sibling(text=True) else ''
    product_info = product_info_tag.find_next_sibling(text=True).strip() if product_info_tag and product_info_tag.find_next_sibling(text=True) else ''
    fabric_info = fabric_info_tag.find_next_sibling(text=True).strip() if fabric_info_tag and fabric_info_tag.find_next_sibling(text=True) else ''
    sample_size = sample_size_tag.find_next('strong').text if sample_size_tag and sample_size_tag.find_next('strong') else ''

    return model_measurements, product_info, fabric_info, sample_size

def transform_data(raw_data):
    transformed_data = []

    for product in raw_data:
        discounted_price = float(product['ProductDetails'].get('DiscountedPrice', 0).replace(',', '.'))
        price = float(product['ProductDetails'].get('Price', 0).replace(',', '.'))
        is_discounted = discounted_price != price and discounted_price != 0
        model_measurements, product_measurements, fabric, sample_size = extract_description_info(product['Description'])
        status = "Active" if int(product['ProductDetails'].get('Quantity', 0)) > 0 else "Inactive"
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
            'SampleSize': sample_size,
            'ModelMeasurements': model_measurements,
            'ProductMeasurements': product_measurements,
            'Status': status,
            'IsDiscounted': is_discounted,
        }

        transformed_data.append(transformed_product)

    return transformed_data

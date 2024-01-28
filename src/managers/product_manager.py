from src.classes.product import Product


def create_product_instance(xml_data):  # Create a Product instance from XML data
    return Product(
        stock_code=xml_data['ProductId'],
        color=xml_data['Color'],
        discounted_price=xml_data['DiscountedPrice'],
        images=xml_data['Images'],
        is_discounted=xml_data['IsDiscounted'],
        name=xml_data['Name'],
        price=xml_data['Price'],
        price_unit=xml_data['PriceUnit'],
        product_type=xml_data['ProductType'],
        quantity=xml_data['Quantity'],
        sample_size=xml_data['SampleSize'],
        series=xml_data['Series'],
        status=xml_data['Status'],
        fabric=xml_data['Fabric'],
        model_measurements=xml_data['ModelMeasurements'],
        product_measurements=xml_data['ProductMeasurements'],
    )


def transform_data_for_mongo(products):  # Transform the data for MongoDB
    return [product.to_dict() for product in products]

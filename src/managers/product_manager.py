from src.classes.product import Product
import os
from dotenv import load_dotenv
from src.helpers.mongo_connection import connect_to_mongodb


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


# Load the .env file
load_dotenv()


def transform_data_for_mongo(products):  # Transform the data for MongoDB
    # Get the variables from .env
    database_name = os.getenv('database_name')
    collection_name = os.getenv('collection_name')

    collection = connect_to_mongodb(database_name, collection_name)
    for product in products:
        product_dict = product.to_dict()
        product_dict.pop('_id', None)
        result = collection.update_one(
            {'stock_code': product_dict['stock_code']},
            {'$set': product_dict},  # the new data
            upsert=True  # if the product doesn't exist, insert it
        )
        print(f"Matched and modified {result.matched_count} documents for product {product_dict['stock_code']}.")

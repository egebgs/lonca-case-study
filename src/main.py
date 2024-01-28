from xml_parser import parse_xml
from data_transformer import transform_data
from mongo_connection import connect_to_mongodb
from src.managers.product_manager import create_product_instance, transform_data_for_mongo

if __name__ == "__main__":
    xml_file_path = '../data/lonca-sample.xml'
    raw_data = parse_xml(xml_file_path)
    transformed_data = transform_data(raw_data)
    products = [create_product_instance(data) for data in transformed_data]
    db_collection = connect_to_mongodb('lonca_db', 'products_collection')
    transformed_products_for_mongo = transform_data_for_mongo(products)

    result = db_collection.insert_many(transformed_products_for_mongo)
    print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")

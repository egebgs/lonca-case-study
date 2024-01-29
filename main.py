import os
from src.helpers.xml_parser import parse_xml
from src.helpers.data_transformer import transform_data
from src.helpers.mongo_connection import connect_to_mongodb
from src.managers.product_manager import create_product_instance, transform_data_for_mongo

if __name__ == "__main__":
    database_name = os.getenv('database_name')
    collection_name = os.getenv('collection_name')
    # For every XML file in the data folder,
    data_folder_path = 'data/'
    xml_files = [f for f in os.listdir(data_folder_path) if f.endswith('.xml')]

    for xml_file in xml_files:
        xml_file_path = os.path.join(data_folder_path, xml_file)
        # parse the XML file,
        raw_data = parse_xml(xml_file_path)
        # transform the data,
        transformed_data = transform_data(raw_data)
        # create Product instances
        products = [create_product_instance(data) for data in transformed_data]
        db_collection = connect_to_mongodb(database_name, collection_name)
        transformed_products_for_mongo = transform_data_for_mongo(products)
        if transformed_products_for_mongo:
            db_collection.insert_many(transformed_products_for_mongo)




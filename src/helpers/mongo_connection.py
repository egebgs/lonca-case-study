from pymongo import MongoClient

def connect_to_mongodb(database_name, collection_name):
    client = MongoClient('localhost', 27017)
    db = client[database_name]
    collection = db[collection_name]
    return collection

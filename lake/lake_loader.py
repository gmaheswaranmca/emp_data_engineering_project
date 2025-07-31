import pandas as pd
from pymongo import MongoClient

def load(df, config):    
    mongo_db_uri = config['mongo_db_uri']
    # connect to MongoDB
    client = MongoClient(mongo_db_uri)
    db = client[config['lake_db_name']]
    collection = db[config['lake_employees_collection']]
    # insert the DataFrame into the MongoDB collection
    collection.delete_many({})  # Clear existing data
    collection.insert_many(df.to_dict('records'))
    print(f"employees loaded successfully into MongoDB `lake` database.")
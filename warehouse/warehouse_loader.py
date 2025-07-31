import pandas as pd
from pymongo import MongoClient

def load(df_employees, df_department_salaries, config):    
    mongo_db_uri = config['mongo_db_uri']
    # connect to MongoDB
    client = MongoClient(mongo_db_uri)
    db = client[config['warehouse_db_name']]
    # employees collection
    collection = db[config['warehouse_employees_collection']]
    # insert the DataFrame into the MongoDB collection
    collection.delete_many({})  # Clear existing data
    collection.insert_many(df_employees.to_dict('records'))
    print(f"employees loaded successfully into MongoDB `warehouse` database.")

    # department_salaries collection
    collection = db[config['warehouse_department_salaries_collection']]
    # insert the DataFrame into the MongoDB collection
    collection.delete_many({})  # Clear existing data
    collection.insert_many(df_department_salaries.to_dict('records'))
    print(f"department_salaries loaded successfully into MongoDB `warehouse` database.")
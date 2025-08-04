import pandas as pd
from pymongo import MongoClient
import os
import requests

config = {
    # Data sets configuration
    'source' : 'api',  # or 'api' 
    'emp_csv_url': "https://raw.githubusercontent.com/gmaheswaranmca/atme2507/main/Day08/de/qn01/emp.csv",
    'api_url' : "http://localhost:5000/employees",
    # File paths for raw and processed data
    'emp_csv_file': "./data/raw/employees.csv",
    'processed_employees_file': "./data/processed/employees.csv",
    'processed_department_salaries_file': "./data/processed/department_salaries.csv",
    # MongoDB configuration
    'mongo_db_uri': "mongodb+srv://mahesh:12345@cluster0.wkvfjw4.mongodb.net/",
    #  Lake MongoDB configuration
    'lake_db_name': "emp_lake_db",
    'lake_employees_collection': "employees",
    #  Warehouse MongoDB configuration
    'warehouse_db_name': "emp_warehouse_db",
    'warehouse_employees_collection': "employees",
    'warehouse_department_salaries_collection': "department_salaries"
}

def load_to_lake(df, config):    
    mongo_db_uri = config['mongo_db_uri']
    # connect to MongoDB
    client = MongoClient(mongo_db_uri)
    db = client[config['lake_db_name']]
    collection = db[config['lake_employees_collection']]
    # insert the DataFrame into the MongoDB collection
    collection.delete_many({})  # Clear existing data
    collection.insert_many(df.to_dict('records'))
    print(f"employees loaded successfully into MongoDB `lake` database.")

def load_to_warehouse(df_employees, df_department_salaries, config):    
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

def load(config, load_fn, dfs, isLake = False):
    employees_df = dfs[0]
    # If loading to lake, only one DataFrame is passed
    if isLake:        
        load_fn(employees_df, config)
    # If loading to warehouse, two DataFrames are passed
    else:
        df_department_salaries = dfs[1]
        load_fn(employees_df, df_department_salaries, config)


def extract(config): 
    file_name = config['emp_csv_file']      
    if os.path.exists(file_name):
        # read the CSV file locally
        url = config['emp_csv_url']
        df = pd.read_csv(url)
        print('Local Employees Data extracted successfully.')
    elif config['source'] == 'csv':
        # read the CSV file from the URL, save locally
        
        df = pd.read_csv(file_name)
        print('URL Employees Data extracted successfully.')
    elif config['source'] == 'api':
        # read API data and save it as csv locally
        url = config['api_url']
        response = requests.get(url)
        employees = response.json()
        df = pd.DataFrame(employees)
        print('API Employees Data extracted successfully.')
    
    return df


def transform(lake_employees_df):
    """
    Transform the employee data by resetting null salaries and calculating department salaries.
    Args:
        lake_employees_df (pd.DataFrame): DataFrame containing employee data.
    """
    # Reset null salaries to avg salary
    avg_salary = lake_employees_df['salary'].mean()
    lake_employees_df['salary'] = lake_employees_df['salary'].fillna(avg_salary)
    print('Transformed the employee data by resetting null salaries and calculating department salaries.')
    # Calculate department salaries
    df_department_salaries = lake_employees_df.groupby('department').agg({'salary': 'sum'}).reset_index()

    return [lake_employees_df, df_department_salaries]

# Main function to orchestrate the ETL process
def main():
    # Extract data
    lake_employees_df = extract(config)
    lake_employees_df.to_csv(os.path.join(os.path.dirname(__file__), config['emp_csv_file']), index=False)
    # Load data to lake
    load(config, load_to_lake, [lake_employees_df], isLake=True)
    # Transform data
    transformed_dfs = transform(lake_employees_df) 
    # Save transformed data to local files
    transformed_dfs[0].to_csv(os.path.join(os.path.dirname(__file__), config['processed_employees_file']), index=False)
    transformed_dfs[1].to_csv(os.path.join(os.path.dirname(__file__), config['processed_department_salaries_file']), index=False)
    # Load transformed data to warehouse
    load(config, load_to_warehouse, transformed_dfs, isLake=False)
    
if __name__ == "__main__":
    main()
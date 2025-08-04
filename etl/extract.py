import os
import pandas as pd 
import requests

def extract_data(config):       
    if os.path.exists(file_name):
        # read the CSV file locally
        url = config['emp_csv_url']
        df = pd.read_csv(url)
        print('Local Employees Data extracted successfully.')
    elif config['source'] == 'csv':
        # read the CSV file from the URL, save locally
        file_name = config['emp_csv_file']
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


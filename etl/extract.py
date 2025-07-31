import os
import pandas as pd 

def extract(config):
    url = config['emp_csv_url']
    file_name = config['emp_csv_file']
    # read the CSV file from the URL, save locally
    if not os.path.exists(file_name):
        df = pd.read_csv(url)
    else:
        df = pd.read_csv(file_name)

    # read the CSV file and return the data
    return df

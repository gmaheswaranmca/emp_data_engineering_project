import os

from config import config

from etl.extract import extract
    
from lake.lake_loader import load as load_to_lake
from warehouse.warehouse_loader import load as load_to_warehouse
from etl.load import load

from etl.transform import transform
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
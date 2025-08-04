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
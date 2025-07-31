def load(config, load_fn, dfs, isLake = False):
    employees_df = dfs[0]
    # If loading to lake, only one DataFrame is passed
    if isLake:        
        load_fn(employees_df, config)
    # If loading to warehouse, two DataFrames are passed
    else:
        df_department_salaries = dfs[1]
        load_fn(employees_df, df_department_salaries, config)
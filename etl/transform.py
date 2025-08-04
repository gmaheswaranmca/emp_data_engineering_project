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
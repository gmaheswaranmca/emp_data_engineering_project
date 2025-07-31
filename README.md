# Data Engineer project on employee data
## Employees data
```Employees.csv 
emp_id,name,department,city,salary,join_date,performance_score
101,Alice,IT,New York,72000,2019-06-15,88
102,Bob,HR,Boston,58000,2020-08-01,77
103,Charlie,Finance,Chicago,67000,2018-01-10,91
104,David,IT,Boston,75000,2017-03-25,85
105,Eve,Finance,New York,69000,2021-07-11,92
106,Frank,IT,Chicago,,2019-11-04,80
107,Grace,Marketing,San Francisco,61000,2020-12-23,84
108,Heidi,IT,San Francisco,74000,2016-10-18,88
109,Ivy,Marketing,Boston,60000,2018-05-29,76
110,John,HR,New York,59000,2021-03-13,79
111,Kate,Finance,Chicago,73000,2019-02-20,89
112,Leo,IT,Boston,77000,2022-01-01,95
113,Mike,Marketing,New York,61000,2017-09-15,82
114,Nina,HR,San Francisco,62000,2016-06-22,80
115,Owen,Finance,Chicago,68000,2018-12-19,73
116,Paul,IT,New York,76000,2021-10-05,90
117,Quinn,Marketing,Boston,,2019-05-30,85
118,Rachel,Finance,San Francisco,71000,2020-04-17,88
119,Steve,HR,Chicago,60000,2021-02-10,81
120,Tina,IT,San Francisco,72000,2018-08-28,87
```
## Departments data 
```Departments.csv
department,manager
IT,Aaron
Finance,Bruce
HR,Clara
Marketing,Derek 
```

## Extract Data
- The path to the employee dataset CSV is:  
  [emp.csv](https://github.com/gmaheswaranmca/atme2507/blob/main/Day08/de/qn01/emp.csv)
- Save the data to the local folder: `./data/raw`
- Load the data to MongoDB: `emp_lake_db`

## Transform Data
- Reset the salary field for records where it is null (Transformed Data 1 : employees)
- Calculate the total salary for each department and sort by salary in descending order (Transformed Data 2 : department_salaries)

## Load Transformed Data
- Save the transformed data to the local folder: `./data/processed`
- Load the transformed data to MongoDB: `emp_warehouse_db`
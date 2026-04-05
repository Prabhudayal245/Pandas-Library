'''
1-select specific columns
  syntax:
    df_name["column name"]   #for selecting a series
    df_name[["column1","column2","column3","..."]]   #for selecting multiple column 

2-filter rows
  syntax:
    df_name[df_name["column"]>value]   #for single condition
    df_name[(df_name["column"]>value)&(df_name["column"]<value)]   #for multiple condition

3- manipulation
synatx:
df_name["col"][row_indexer] = value
'''

import pandas as pd 
dict1={
    "Name":["ram","shyam","ghansyam","radhe","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,30,29,24,32,40,37],
    "salary":[45000,35000,60000,28000,70000,55000,65000,30000],
    "performance_score":[86,84,89,93,82,97,91,88],
}

data=pd.DataFrame(dict1)
print("Displaying the dataframe:")
print(data)

#selecting single column
print("Name (single column return series)")
print(data["Name"])

#selecting multiple columns
print("multiple columns")
print(data[["Name","Age","salary"]])

#single condition
filter_row=data[data["salary"]>50000]
print("Salary,which have a more than 50000:")
print(filter_row)

#using AND condition
filter_rows=data[(data["salary"]>50000)&(data["Age"]>30)]
print("Salary more than 50000 as well as age is more than 30:")
print(filter_rows)

#using OR condition
filter_rowss=data[(data["salary"]>50000)|(data["performance_score"]<90)]
print("salary greater than 50000 or performance_score is less than 30")
print(filter_rowss)
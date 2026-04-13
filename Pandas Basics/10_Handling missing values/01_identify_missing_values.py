'''
isnull():It is used to identify the missing value in the dataframe.it return boolean (True/False) value.
'''
import pandas as pd

dict1={
    "Name":["ram","shyam",None,"ghansyam","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,33,30,24,32,40,37],
    "salary":[45000,35000,None,60000,70000,55000,65000,30000],
    "performance_score":[86,84,None,89,82,97,91,88],
}

data=pd.DataFrame(dict1)
print(data.isnull())
print(data.isnull().sum())
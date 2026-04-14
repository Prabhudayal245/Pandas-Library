'''
fillna:it is use to fill the values in missing place.
syntax:
df_name.fillna(value,inplace=True)
'''

import pandas as pd

dict1={
    "Name":["ram","shyam",None,"ghansyam","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,None,30,24,32,40,37],
    "salary":[45000,35000,None,60000,70000,55000,65000,30000],
    "performance_score":[86,84,None,89,82,97,91,88],
}

data=pd.DataFrame(dict1)
data["Name"].fillna("radhe",inplace=True)
data["Age"].fillna(data["Age"].mean(),inplace=True)
data["salary"].fillna(data["salary"].mean(),inplace=True)
data["performance_score"].fillna(data["performance_score"].mean(),inplace=True)
print(data)
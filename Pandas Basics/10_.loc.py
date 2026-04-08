'''
.loc[]:It use for data manipulation or updating the data.

Syntax:
df_name.loc[row_index,"column_name"]=new_value
'''

import pandas as pd

dict1={
    "Name":["ram","shyam","ghansyam","radhe","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,30,29,24,32,40,37],
    "salary":[45000,35000,60000,28000,70000,55000,65000,30000],
    "performance_score":[86,84,89,93,82,97,91,88],
}

data=pd.DataFrame(dict1)
print("Old data")
print(data)

#updating 
data.loc[0,"salary"]=50000
print("New data")
print(data)

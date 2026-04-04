'''
Shape:it give the number of rows and columns in the data set .
columns:it gives the name of columns in the data set
'''
import pandas as pd
dict1={
    "Name":["ram","shyam","ghansyam","radhe","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,30,29,24,32,40,37],
    "salary":[45000,35000,60000,28000,70000,55000,65000,30000],
    "performance_score":[86,84,89,93,82,97,91,88],
}

data=pd.DataFrame(dict1)
print(data)
print("Displaying the number of rows and columns in tuple.")
print(f"Shape:{data.shape}")
print("displaying the name of columns name:")
print(f"columns name:{data.columns}")

'''
adding column:
  syntax:
  1-df_name["column_name"]=some_data   #It add the column at the  end of data
  2-df_name.insert(index_no,"column_name","data")
'''

import pandas as pd

dict1={
    "Name":["ram","shyam","ghansyam","radhe","nayan","jagdish","rajesh","somya"],
    "Age":[35,25,30,29,24,32,40,37],
    "salary":[45000,35000,60000,28000,70000,55000,65000,30000],
    "performance_score":[86,84,89,93,82,97,91,88],
}

data=pd.DataFrame(dict1)
print("Sample data")
print(data)

#add column 
data["Bonus"]=data["salary"]*0.1  # adding column by normal method.
print(data)

#Using Insert mathod
data.insert(0,"EmpID",["E1","E2","E3","E4","E5","E6","E7","E8"])  
print(data)
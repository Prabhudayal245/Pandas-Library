import pandas as pd

data={
    "Name":["Arun","Kaif","Manish","Prabhu"],
    "Age":[19,18,20,17],
    "salary":[30000,40000,34000,45000]
}

df=pd.DataFrame(data)
print("Sample DataFrame")
print(df)


df.sort_values(by="salary",ascending=True,inplace=True)  #single column  are sort
print("sorted salary")
print(df)


df.sort_values(by=["Age","salary"],ascending=[True,False],inplace=True)  #multiple column  are sort
print(df)
import pandas as pd
employees = {
    "Name": ["Anshu","Jay","Alina","Soni","Ava","Vivek","Radhika","Diya"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","IT"],
    "City": ["Delhi","Delhi","Mumbai","Mumbai","Delhi","Mumbai","Delhi","Delhi"],
    "Salary": [50000,60000,55000,70000,58000,62000,68000,65000]
}

df=pd.DataFrame(employees)
print(df)

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].sum())
print(df.groupby("Department").count())
print(df.groupby(["Department","City"])["Salary"].mean())
print(df[["Department","City"]].value_counts())
print(df.groupby("Department")["Salary"].agg(["mean","max","min"]))

result=df.groupby("Department").value_counts().reset_index()
print(result)

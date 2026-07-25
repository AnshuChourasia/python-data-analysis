import pandas as pd
employees = {
    "ID":[1,2,3,4,5,6],
    "Name":["Anshu","Jay","Alina","Soni","Ava","Vivek"],
    "Department":["IT","HR","IT","Finance","HR","IT"],
    "Salary":[50000,60000,None,55000,58000,62000]
}
df=pd.DataFrame(employees)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df["Name"])
print(df[["Name","Salary"]])
print(df[df["Salary"]>55000])
print(df[df["Department"]=="IT"])
print(df.sort_values(by="Salary",ascending=False))
print(df[(df["Salary"]>52000) & (df["Salary"]<57000)])
print(df[
    ((df["Department"]=="IT") | (df["Department"]=="HR")) & (df["Salary"]>55000)
    ])
print(df["Salary"].mean())
highest_salary=df.sort_values(by="Salary",ascending=False)
print(highest_salary.head(3))
print(df["Department"].value_counts())

print(df.isnull())
print(df.isnull().sum())
df=df.fillna(df["Salary"].mean())
df["Salary"]+=3000
df["Bonus"]=df["Salary"] * 0.10
df["Tax"]=df["Salary"] * 0.05
print(df)

df.rename(columns={
          "Department":"Team",
          "Salary":"Monthly Salary"},inplace=True)
df.drop(columns=["Tax"],inplace=True)

df.to_csv("employee_report.csv",index=False)

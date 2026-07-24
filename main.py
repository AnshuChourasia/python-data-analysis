import pandas as pd
employees = {
    "ID":[1,2,3,4,5,6,7,8,9,10],
    "Name":["Anshu","Jay","Alina","Soni","Ava","Baby","Vivek","Radhika","Laila","Diya"],
    "Department":["IT","HR","Finance","Eco","IT","HR","Eco","Finance","Commerce","Commerce"],
    "Salary":[60000,54000,52000,53000,54000,55000,56000,57000,58000,59000]
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
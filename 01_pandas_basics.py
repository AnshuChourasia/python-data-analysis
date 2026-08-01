"""
Day 6 – Pandas Basics

Topics Covered:
- Creating DataFrames
- Data Exploration
- Filtering & Sorting
- Handling Missing Values
- Feature Engineering
- Renaming Columns
- Exporting Data

Author: Anshu Chourasia
"""

import pandas as pd

# ==========================================
# Create Employee DataFrame
# ==========================================

employees = {
    "ID": [1, 2, 3, 4, 5, 6],
    "Name": ["Anshu", "Jay", "Alina", "Soni", "Ava", "Vivek"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 60000, None, 55000, 58000, 62000]
}

df = pd.DataFrame(employees)

# ==========================================
# Display Dataset
# ==========================================

print("Complete DataFrame:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# Selecting Columns
# ==========================================

print("\nEmployee Names:")
print(df["Name"])

print("\nEmployee Names and Salaries:")
print(df[["Name", "Salary"]])

# ==========================================
# Filtering Data
# ==========================================

print("\nEmployees with Salary Greater Than 55000:")
print(df[df["Salary"] > 55000])

print("\nEmployees from IT Department:")
print(df[df["Department"] == "IT"])

print("\nEmployees with Salary Between 52000 and 57000:")
print(df[(df["Salary"] > 52000) & (df["Salary"] < 57000)])

print("\nEmployees from IT or HR Department with Salary Greater Than 55000:")
print(
    df[
        ((df["Department"] == "IT") | (df["Department"] == "HR"))
        & (df["Salary"] > 55000)
    ]
)

# ==========================================
# Sorting Data
# ==========================================

print("\nEmployees Sorted by Salary (Highest First):")
print(df.sort_values(by="Salary", ascending=False))

# ==========================================
# Statistics
# ==========================================

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nTop 3 Highest Paid Employees:")
top_3_salary = df.nlargest(3, "Salary")
print(top_3_salary)

print("\nNumber of Employees in Each Department:")
print(df["Department"].value_counts())

# ==========================================
# Handling Missing Values
# ==========================================

print("\nMissing Values:")
print(df.isnull())

print("\nMissing Value Count:")
print(df.isnull().sum())

# Fill missing salary with average salary
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# ==========================================
# Feature Engineering
# ==========================================

# Increase salary by 3000
df["Salary"] += 3000

# Add Bonus column (10% of salary)
df["Bonus"] = df["Salary"] * 0.10

# Add Tax column (5% of salary)
df["Tax"] = df["Salary"] * 0.05

print("\nUpdated Employee Data:")
print(df)

# ==========================================
# Rename Columns
# ==========================================

df.rename(
    columns={
        "Department": "Team",
        "Salary": "Monthly Salary"
    },
    inplace=True
)

# ==========================================
# Drop Unnecessary Columns
# ==========================================

df.drop(columns=["Tax"], inplace=True)

print("\nFinal Employee Report:")
print(df)

# ==========================================
# Export Data
# ==========================================

# Save the cleaned dataset as a CSV file
df.to_csv("employee_report.csv", index=False)

print("\nEmployee report exported successfully as 'employee_report.csv'.")
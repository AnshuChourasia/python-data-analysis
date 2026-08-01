"""
Day 7 – GroupBy & Aggregation

Topics Covered:
- GroupBy
- Mean, Maximum & Sum
- Multiple Grouping
- Value Counts
- Aggregation Functions
- Reset Index

Author: Anshu Chourasia
"""

import pandas as pd

# ==========================================
# Create Employee DataFrame
# ==========================================

employees = {
    "Name": [
        "Anshu", "Jay", "Alina", "Soni",
        "Ava", "Vivek", "Radhika", "Diya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "IT", "Finance", "IT"
    ],
    "City": [
        "Delhi", "Delhi", "Mumbai", "Mumbai",
        "Delhi", "Mumbai", "Delhi", "Delhi"
    ],
    "Salary": [
        50000, 60000, 55000, 70000,
        58000, 62000, 68000, 65000
    ]
}

df = pd.DataFrame(employees)

print("Employee Dataset")
print(df)

# ==========================================
# Problem 1: Average Salary by Department
# ==========================================

print("\nAverage Salary by Department")
print(df.groupby("Department")["Salary"].mean())

# ==========================================
# Problem 2: Maximum Salary by Department
# ==========================================

print("\nMaximum Salary by Department")
print(df.groupby("Department")["Salary"].max())

# ==========================================
# Problem 3: Total Salary by Department
# ==========================================

print("\nTotal Salary by Department")
print(df.groupby("Department")["Salary"].sum())

# ==========================================
# Problem 4: Number of Employees in Each Department
# ==========================================

print("\nEmployee Count by Department")
print(df.groupby("Department").count())

# ==========================================
# Problem 5: Average Salary by Department and City
# ==========================================

print("\nAverage Salary by Department and City")
print(df.groupby(["Department", "City"])["Salary"].mean())

# ==========================================
# Problem 6: Count Department and City Combinations
# ==========================================

print("\nDepartment-City Combination Counts")
print(df[["Department", "City"]].value_counts())

# ==========================================
# Problem 7: Multiple Aggregations
# ==========================================

print("\nMean, Maximum and Minimum Salary")
print(
    df.groupby("Department")["Salary"].agg(
        ["mean", "max", "min"]
    )
)

# ==========================================
# Problem 8: GroupBy with Reset Index
# ==========================================

result = df.groupby("Department").value_counts().reset_index()

print("\nGrouped Data with Reset Index")
print(result)
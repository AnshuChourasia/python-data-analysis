"""
Merge, Concat & DateTime Handling

Topics Covered:
- Merge & Join
- Concat
- Date & Time Handling

Dataset:
Custom DataFrames

Author: Anshu Chourasia
"""
import pandas as pd

# ==========================================
# Day 16 – Merge & Join
# ==========================================

# Employee Data
employees = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["John", "Alice", "Bob", "David"]
})

# Salary Data
salaries = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Salary": [50000, 60000, 55000, 70000]
})

# City Data
city = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Pune", "Chennai"]
})

# New Employees
new_employees = pd.DataFrame({
    "ID": [5, 6],
    "Name": ["Emma", "Chris"]
})

# ==========================================
# Problem 1: Inner Join
# ==========================================

print(pd.merge(employees, salaries, on="ID"))

# ==========================================
# Problem 2: Left Join
# ==========================================

print(pd.merge(employees, salaries, on="ID", how="left"))

# ==========================================
# Problem 3: Right Join
# ==========================================

print(pd.merge(employees, salaries, on="ID", how="right"))

# ==========================================
# Problem 4: Outer Join
# ==========================================

print(pd.merge(employees, salaries, on="ID", how="outer"))

# ==========================================
# Problem 5: Horizontal Concatenation
# ==========================================

print(pd.concat([employees, city], axis=1))

# ==========================================
# Problem 6: Vertical Concatenation
# ==========================================

print(pd.concat([employees, new_employees], ignore_index=True))

# ==========================================
# Bonus Challenges
# ==========================================

merged_df = pd.merge(employees, salaries, on="ID", how="outer")

print(merged_df)

# Employees with missing salary
print(
    f"The names of employees with missing salary are: "
    f"{merged_df[merged_df['Salary'].isnull()]['Name'].tolist()}"
)

# Count employees with missing salary
print(
    f"The number of employees with missing salary is: "
    f"{merged_df['Salary'].isnull().sum()}"
)

# ==========================================
# Day 17 – Date & Time Handling
# ==========================================

df = pd.DataFrame({
    "Employee": ["John", "Alice", "Bob", "David"],
    "Joining_Date": [
        "2020-05-15",
        "2021-08-10",
        "2019-12-20",
        "2023-02-01"
    ]
})

# Convert Joining_Date column to datetime format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

# ==========================================
# Problem 1: Display Joining Year
# ==========================================

print(df["Joining_Date"].dt.year)

# ==========================================
# Problem 2: Display Joining Month
# ==========================================

print(df["Joining_Date"].dt.month)

# ==========================================
# Problem 3: Display Day Name
# ==========================================

print(df["Joining_Date"].dt.day_name())

# ==========================================
# Problem 4: Calculate Days Since Joining
# ==========================================

today = pd.Timestamp.today()

days_since_joining = (today - df["Joining_Date"]).dt.days

print(days_since_joining)

# ==========================================
# Problem 5: Sort by Joining Date (Oldest First)
# ==========================================

print(df.sort_values(by="Joining_Date"))

# ==========================================
# Problem 6: Sort by Joining Date (Newest First)
# ==========================================

print(df.sort_values(by="Joining_Date", ascending=False))

# ==========================================
# Problem 7: Employees Joined After 2021-01-01
# ==========================================

print(df[df["Joining_Date"] >= "2021-01-01"])

# ==========================================
# Bonus 1: Employees Joined Before 2021
# ==========================================

print(df[df["Joining_Date"] < "2021-01-01"])

# ==========================================
# Bonus 2: Employee Who Joined Earliest
# ==========================================

print(df.nsmallest(1, "Joining_Date"))

# ==========================================
# Bonus 3: Employee Who Joined Most Recently
# ==========================================

print(df.nlargest(1, "Joining_Date"))

# ==========================================
# Bonus 4: Create Joining_Year Column
# ==========================================

df["Joining_Year"] = df["Joining_Date"].dt.year

print(df)

# ==========================================
# Bonus 5: Count Employees by Joining Year
# ==========================================

print(df["Joining_Year"].value_counts())
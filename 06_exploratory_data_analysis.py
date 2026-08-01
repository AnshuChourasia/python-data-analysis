"""
Exploratory Data Analysis (EDA) – Titanic Dataset

Topics Covered:
- Basic Data Exploration
- Filtering & Sorting
- Pivot Tables
- Crosstabs

Dataset:
Titanic Dataset (Seaborn)

Author: Anshu Chourasia
"""

import pandas as pd
import seaborn as sns

# ==========================================
# Load Dataset
# ==========================================

df = sns.load_dataset("titanic")

# Display first 5 rows
print(df.head())

# =====================================================
# Day 11 – Basic Data Exploration
# =====================================================

# 1. Count survivors
print(df["survived"].value_counts())

# 2. Average age
print(df["age"].mean())

# 3. Count male and female passengers
print(df["sex"].value_counts())

# 4. Passenger class with highest average fare
print(df.groupby("pclass")["fare"].mean().idxmax())

# 5. Column with the most missing values
print(df.isnull().sum().idxmax())

# 6. Passenger class with highest survival rate
print(df.groupby("pclass")["survived"].mean().idxmax())

# 7. Gender with highest survival rate
print(df.groupby("sex")["survived"].mean().idxmax())

# 8. Passenger class with highest average age
print(df.groupby("pclass")["age"].mean().idxmax())

# 9. Number of passengers in each class
print(df["pclass"].value_counts())

# 10. Most common embarkation port
print(df["embarked"].value_counts().idxmax())

# 11. Passenger class with most survivors
print(df.groupby("pclass")["survived"].sum().idxmax())

# 12. Average fare by gender
print(df.groupby("sex")["fare"].mean())

# 13. Gender paying the highest average fare
print(df.groupby("sex")["fare"].mean().idxmax())

# 14. Passenger class with the most female passengers
print(df[df["sex"] == "female"]["pclass"].value_counts().idxmax())

# 15. Embarkation port with the highest average fare
print(df.groupby("embarked")["fare"].mean().idxmax())

# 16. Number of children (Age < 18)
print((df["age"] < 18).sum())

# =====================================================
# Day 12 – Filtering & Sorting
# =====================================================

# 1. Display all female passengers
print(df[df["sex"] == "female"])

# 2. Display passengers older than 50
print(df[df["age"] > 50])

# 3. Female passengers who survived
print(df[(df["sex"] == "female") & (df["survived"] == 1)])

# 4. Passengers in First or Second Class
print(df[df["pclass"].isin([1, 2])])

# 5. Passengers whose fare is between 20 and 100
print(df[df["fare"].between(20, 100)])

# 6. Sort passengers by age (oldest first)
print(df.sort_values("age", ascending=False))

# 7. Top 10 highest fares
print(df.nlargest(10, "fare"))

# 8. Male survivors older than 30
print(df[(df["age"] > 30) &
         (df["survived"] == 1) &
         (df["sex"] == "male")])

# 9. Female passengers in Third Class
print(df[(df["sex"] == "female") & (df["pclass"] == 3)])

# 10. Passengers aged between 18 and 40 with fare > 50
print(df[df["age"].between(18, 40) & (df["fare"] > 50)])

# 11. Youngest 10 passengers
print(df.nsmallest(10, "age"))

# 12. Passengers who embarked from S or C
print(df[df["embarked"].isin(["S", "C"])])

# =====================================================
# Day 13 – Pivot Tables & Crosstabs
# =====================================================

# Average age by passenger class
print(pd.pivot_table(df, values="age", index="pclass"))

# Average fare by gender
print(pd.pivot_table(df, values="fare", index="sex"))

# Maximum fare by passenger class
print(pd.pivot_table(df, values="fare", index="pclass", aggfunc="max"))

# Average age by passenger class and gender
print(pd.pivot_table(df, values="age", index=["pclass", "sex"]))

# Average fare by passenger class (columns = gender)
print(pd.pivot_table(df, values="fare", index="pclass", columns="sex"))

# Mean, Maximum and Minimum fare by passenger class
print(pd.pivot_table(df,
                     values="fare",
                     index="pclass",
                     aggfunc=["mean", "max", "min"]))

# Crosstab: Gender vs Survival
print(pd.crosstab(df["sex"], df["survived"]))

# Crosstab: Passenger Class vs Survival
print(pd.crosstab(df["pclass"], df["survived"]))

# Average fare by embarkation port
print(pd.pivot_table(df, values="fare", index="embarked"))

# Maximum age by gender
print(pd.pivot_table(df, values="age", index="sex", aggfunc="max"))

# Count of passengers in each passenger class
print(pd.pivot_table(df, values="fare", index="pclass", aggfunc="count"))

# Crosstab: Passenger Class vs Gender
print(pd.crosstab(df["pclass"], df["sex"]))
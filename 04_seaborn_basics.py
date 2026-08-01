"""
Day 11 – Seaborn Basics

Topics Covered:
- Count Plot
- Bar Plot
- Histogram
- Scatter Plot
- Box Plot
- Heatmap

Dataset:
Tips Dataset (Seaborn)

Author: Anshu Chourasia
"""

import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# Load Dataset
# ==========================================

tips = sns.load_dataset("tips")

print("First 5 Rows of Tips Dataset:")
print(tips.head())

# ==========================================
# Correlation Matrix
# ==========================================

corr = tips.corr(numeric_only=True)

# ==========================================
# Problem 1: Count Plot
# Number of customers visiting each day
# ==========================================

sns.countplot(
    data=tips,
    x="day"
)

plt.title("Number of Customers by Day")
plt.show()

# ==========================================
# Problem 2: Bar Plot
# Average Total Bill by Day
# ==========================================

sns.barplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Average Total Bill by Day")
plt.show()

# ==========================================
# Problem 3: Histogram
# Distribution of Total Bill
# ==========================================

sns.histplot(
    data=tips,
    x="total_bill"
)

plt.title("Distribution of Total Bill")
plt.show()

# ==========================================
# Problem 4: Scatter Plot
# Relationship Between Total Bill and Tip
# ==========================================

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="smoker"
)

plt.title("Total Bill vs Tip")
plt.show()

# ==========================================
# Problem 5: Box Plot
# Total Bill Distribution by Day
# ==========================================

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.title("Total Bill Distribution by Day")
plt.show()

# ==========================================
# Problem 6: Heatmap
# Correlation Between Numerical Features
# ==========================================

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()
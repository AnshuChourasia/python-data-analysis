"""
Day 10 – Matplotlib Basics

Topics Covered:
- Line Plot
- Bar Chart
- Pie Chart
- Histogram
- Scatter Plot

Author: Anshu Chourasia
"""

import matplotlib.pyplot as plt

# ==========================================
# Problem 1: Monthly Sales Line Plot
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 17000, 22000, 25000, 30000]

plt.plot(
    months,
    sales,
    color="green",
    linestyle="--",
    marker="o"
)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# ==========================================
# Problem 2: Employees by Department (Bar Chart)
# ==========================================

departments = ["IT", "HR", "Finance", "Marketing"]
employees = [25, 15, 20, 10]

plt.bar(
    departments,
    employees,
    color="blue"
)

plt.title("Employees in Departments")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.show()

# ==========================================
# Problem 3: Expense Distribution (Pie Chart)
# ==========================================

expenses = [40, 30, 20, 10]
labels = ["Salary", "Rent", "Marketing", "Misc"]

plt.pie(
    expenses,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Expense Distribution")
plt.show()

# ==========================================
# Problem 4: Salary Distribution (Histogram)
# ==========================================

salary = [42000, 52000, 65000, 71000]

plt.hist(
    salary,
    bins=5
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# ==========================================
# Problem 5: Experience vs Salary
# (Scatter Plot with Trend Line)
# ==========================================

experience = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salary = [25000, 30000, 36000, 42000, 50000,
          58000, 65000, 72000, 80000, 90000]

# Scatter plot
plt.scatter(
    experience,
    salary,
    color="red",
    label="Employees"
)

# Line showing trend
plt.plot(
    experience,
    salary,
    color="blue",
    label="Trend"
)

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.legend()
plt.show()
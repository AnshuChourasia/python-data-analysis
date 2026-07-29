# Pandas GroupBy and Aggregation

This project demonstrates how to perform data analysis using **Pandas GroupBy** and aggregation functions. It focuses on summarizing employee data by department and city to generate meaningful insights.

## Features

* Create a Pandas DataFrame
* Group employees by department
* Calculate average salary by department
* Calculate total salary by department
* Find the highest salary in each department
* Find the lowest salary in each department
* Count employees in each department
* Group data by multiple columns (Department and City)
* Count occurrences using `value_counts()`
* Perform multiple aggregations using `agg()`
* Convert grouped indexes back into columns using `reset_index()`

## Technologies Used

* Python 3
* Pandas

## Dataset

The project uses a sample employee dataset containing:

* Employee Name
* Department
* City
* Salary

## Pandas Concepts Practiced

* `groupby()`
* `mean()`
* `sum()`
* `max()`
* `min()`
* `count()`
* `agg()`
* Multi-column grouping
* `value_counts()`
* `reset_index()`

## How to Run

1. Install Pandas

```bash
pip install pandas
```

2. Run the program

```bash
python main.py
```

## Project Tasks

* Calculate average salary by department
* Calculate total salary by department
* Find highest and lowest salary in each department
* Count employees in each department
* Analyze salaries by Department and City
* Count employees by city
* Perform multiple aggregations using `agg()`
* Convert grouped results into a regular DataFrame using `reset_index()`

# Learning Progress

- ✅ Day 7 - Pandas Basics
- ✅ Day 8 - Data Cleaning & Manipulation
- ✅ Day 9 - GroupBy & Aggregation
- ✅ Day 10 - Data Visualization with Matplotlib
- ⬜ Day 11 - Seaborn
- ⬜ Day 12 - NumPy
- ⬜ Day 13 - Exploratory Data Analysis (EDA)
- ⬜ Day 14 - Mini Data Analysis Project
- ⬜ Day 15 - Final Project

## Learning Outcomes

Through this project, I learned:

* How to summarize data using `groupby()`.
* How to calculate multiple statistics for grouped data.
* The difference between `groupby()` and `value_counts()`.
* How to group data using more than one column.
* How to create summary tables using `agg()`.
* Why `reset_index()` is useful after grouping.

## Future Improvements

* Merge multiple datasets
* Create Pivot Tables
* Visualize grouped data using Matplotlib
* Build interactive dashboards

---
Data Visualization with Seaborn

## 📌 Overview

I learned the basics of **Seaborn**, a Python library built on top of Matplotlib that provides beautiful and statistical data visualizations with less code.

## 📚 Topics Covered

- Loading built-in datasets
- Count Plot
- Bar Plot
- Histogram
- Scatter Plot
- Box Plot
- Heatmap
- Correlation Matrix
- Hue
- Annotation
- Color Maps

## 🛠 Libraries Used

```python
import seaborn as sns
import matplotlib.pyplot as plt

NumPy Basics and Array Operations

## 📌 Overview

I learned **NumPy (Numerical Python)**, a Python library used for fast numerical computations. NumPy provides powerful array operations and mathematical functions that are widely used in Data Science, Machine Learning, and Scientific Computing.

---

## 📚 Topics Covered

- Introduction to NumPy
- Creating NumPy Arrays
- Vectorized Operations
- Array Indexing
- Array Slicing
- Mathematical Functions
- 2D Arrays (Matrices)
- Array Shape

---

## 🛠 Library Used

```python
import numpy as np
```

---

## Concepts Learned

### 1. Creating Arrays

Created arrays using:

```python
np.array()
np.zeros()
np.ones()
np.arange()
```

Example:

```python
arr = np.array([10,20,30,40,50])
```

---

### 2. Vectorized Operations

Performed mathematical operations without using loops.

```python
arr + 10
arr * 3
arr - 5
arr / 2
```

---

### 3. Mathematical Functions

Used built-in NumPy functions:

```python
np.sum(arr)
np.mean(arr)
np.max(arr)
np.min(arr)
np.std(arr)
```

These functions help perform calculations quickly on arrays.

---

### 4. Indexing and Slicing

Accessing elements:

```python
arr[0]
arr[-1]
```

Slicing arrays:

```python
arr[:3]
arr[2:]
arr[1:4]
```

---

### 5. 2D Arrays (Matrices)

Created a matrix:

```python
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
```

Accessed:

- Individual elements
- Entire rows
- Entire columns

Example:

```python
matrix[0]
matrix[:,1]
matrix.shape
```

---

## Practical Exercise Completed

Implemented a NumPy program that:

- Created arrays
- Performed vectorized arithmetic
- Calculated:
  - Sum
  - Mean
  - Maximum
  - Minimum
  - Standard Deviation
- Created and accessed a 3×3 matrix
- Generated arrays using:
  - `np.zeros()`
  - `np.ones()`
  - `np.arange()`

---

## Key Learnings

- NumPy is much faster than Python lists for numerical computations.
- Arrays are the core data structure of NumPy.
- Vectorized operations eliminate the need for loops.
- NumPy provides powerful built-in mathematical functions.
- 2D arrays allow easy matrix manipulation.
- Indexing and slicing work similarly to Python lists but extend naturally to multiple dimensions.

---

## Learning Outcome

After completing Day 12, I can:

- Work with NumPy arrays.
- Perform fast mathematical operations.
- Use vectorized calculations.
- Create and manipulate matrices.
- Apply built-in statistical functions.
- Access and slice 1D and 2D arrays efficiently.

---

---


**Author:** Anshu Chourasia

# Pandas Data Cleaning and Manipulation

This project focuses on **data cleaning and manipulation using Pandas**, an essential step in every data analysis workflow. It demonstrates how to detect and handle missing values, modify DataFrames, create new columns, and export cleaned data to a CSV file.

## Features

* 📊 Create a Pandas DataFrame
* 🔍 Detect missing values using `isnull()`
* 📈 Count missing values with `isnull().sum()`
* 🗑 Remove missing values using `dropna()`
* ✨ Fill missing values using `fillna()`
* ➕ Add new columns (Bonus and Tax)
* ✏️ Modify existing columns
* 📝 Rename columns
* ❌ Delete columns
* 🔃 Sort employees by salary
* 🏆 Display the top 3 highest-paid employees
* 💰 Calculate the average salary
* 👥 Count employees in each department
* 💾 Export the cleaned DataFrame to a CSV file

## Technologies Used

* Python 3
* Pandas

## Dataset

The project uses a sample employee dataset containing:

* Employee ID
* Employee Name
* Department
* Salary

Some records intentionally contain missing values (`NaN`) to demonstrate data cleaning techniques.

## Pandas Concepts Practiced

* `DataFrame`
* `isnull()`
* `isnull().sum()`
* `dropna()`
* `fillna()`
* Column Creation
* Column Modification
* `rename()`
* `drop()`
* `sort_values()`
* `head()`
* `mean()`
* `value_counts()`
* `to_csv()`

## How to Run

1. Install Pandas:

```bash
pip install pandas
```

2. Run the program:

```bash
python main.py
```

## Project Tasks

* Detect missing values in the dataset
* Count missing values in each column
* Handle missing values by removing or replacing them
* Create **Bonus** and **Tax** columns
* Increase employee salaries
* Rename selected columns
* Delete unnecessary columns
* Display the top 3 highest-paid employees
* Calculate the average salary
* Count employees by department
* Save the cleaned dataset as a CSV file

## Learning Outcomes

Through this project, I learned:

* How to identify missing values in a dataset.
* Different techniques for handling missing data.
* How to add, update, rename, and delete DataFrame columns.
* How Pandas performs vectorized operations without explicit loops.
* How to sort and analyze tabular data efficiently.
* How to export processed data using `to_csv()`.
* Why data cleaning is an important step before performing analysis.

## Future Improvements

* Read datasets directly from CSV files using `read_csv()`
* Perform advanced grouping using `groupby()`
* Merge multiple datasets
* Handle duplicate records
* Visualize cleaned data using Matplotlib and Seaborn
* Build a complete employee analytics dashboard

---

**Author:** Anshu Chourasia

# Titanic Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset using Python.

The objective is to understand passenger demographics, survival patterns, ticket fares, and relationships between different variables using statistical analysis and data visualization.

---

## Dataset

- Source: Seaborn Titanic Dataset
- Rows: 891
- Columns: 15

---

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Tasks Performed

- Loaded and explored the dataset
- Checked missing values and duplicates
- Filled missing values
- Removed unnecessary columns
- Performed statistical analysis
- Grouped and compared passenger data
- Created visualizations
- Drew conclusions from the data

---

## Visualizations

- Age Distribution Histogram
- Survival Count Plot
- Passenger Class Count Plot
- Fare by Passenger Class (Boxplot)
- Age vs Fare (Scatterplot)
- Correlation Heatmap

---

## Key Insights

- Female passengers had a higher survival rate than male passengers.
- First-class passengers paid the highest fares.
- Southampton was the most common embarkation port.
- Passenger class had a strong relationship with survival.
- Fare varied significantly across passenger classes.

---

## Project Structure

```
08_titanic_eda_project/
│
├── titanic_eda.py
├── README.md
└── plots/
```

---

## How to Run

```bash
pip install pandas numpy matplotlib seaborn

python titanic_eda.py
```
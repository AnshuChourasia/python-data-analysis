# 📺 Netflix Movies & TV Shows - Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on the Netflix Movies and TV Shows dataset using **Python, Pandas, Matplotlib, and Seaborn**.

The objective is to clean the dataset, analyze trends, and visualize key insights such as content distribution, ratings, countries, genres, directors, and release trends.

---

## 📂 Dataset

- **Dataset:** Netflix Movies and TV Shows
- **Source:** Kaggle
- **Format:** CSV

---

## 🛠️ Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pathlib

---

## 📊 Project Workflow

### 1. Data Exploration

- Loaded the dataset
- Examined dataset information
- Checked dataset shape
- Generated descriptive statistics
- Identified missing values

### 2. Data Cleaning

- Filled missing values in:
  - Director
  - Cast
  - Country
  - Rating
  - Duration
- Converted `date_added` to datetime format
- Extracted `added_year`
- Removed duplicate records

### 3. Exploratory Data Analysis

Performed analysis on:

- Movies vs TV Shows
- Most common ratings
- Top 10 Directors
- Top 10 Countries
- Top 10 Genres
- Content released by year
- Content added to Netflix by year
- Oldest titles
- Newest titles
- Average release year
- Year with the highest number of releases

---

## 📈 Visualizations

The project generates and saves the following plots inside the **plots/** folder:

- Movies vs TV Shows
- Rating Distribution
- Top 10 Countries
- Release Trend
- Top 10 Genres
- Top 10 Directors

---

## 🔍 Key Insights

- Netflix contains significantly more **Movies** than **TV Shows**.
- **TV-14** is the most common content rating.
- The **United States** contributes the largest amount of content.
- Content production increased rapidly after **2015**.
- Drama and International content dominate the platform.

---

## 📁 Project Structure

```
09_netflix_eda_project/
│
├── netflix_eda.py
├── netflix_titles.csv
├── README.md
└── plots/
    ├── movies_vs_tvshows.png
    ├── rating_distribution.png
    ├── top_countries.png
    ├── release_trend.png
    ├── top_genres.png
    └── top_directors.png
```

---

## 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/AnshuChourasia/python-data-analysis.git
```

Move into the project folder

```bash
cd python-data-analysis/09_netflix_eda_project
```

Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

Run the project

```bash
python netflix_eda.py
```

---

## 📚 Skills Demonstrated

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Exploratory Data Analysis
- Data Visualization
- Python Programming
- Pandas
- Matplotlib
- Seaborn

---

## 👨‍💻 Author

**Anshu Chourasia**

GitHub: https://github.com/AnshuChourasia
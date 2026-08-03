import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# ==========================================
# Setup
# ==========================================

plot_dir = Path(__file__).parent / "plots"
plot_dir.mkdir(exist_ok=True)

df = pd.read_csv("netflix_titles.csv")

# ==========================================
# Step 1: Initial Exploration
# ==========================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFO ==========")
df.info()

print("\n========== DESCRIPTION ==========")
print(df.describe())

print("\nDataset Shape:", df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# ==========================================
# Step 2: Data Cleaning
# ==========================================

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
df["duration"] = df["duration"].fillna("Unknown")

df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

df["added_year"] = df["date_added"].dt.year

df.drop_duplicates(inplace=True)

print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(df.isnull().sum())

# ==========================================
# Step 3: Exploratory Data Analysis
# ==========================================

print("\n========== MOVIES VS TV SHOWS ==========")
print(df["type"].value_counts())

print("\n========== TOP RATINGS ==========")
print(df["rating"].value_counts().head(10))

print("\n========== TOP 10 DIRECTORS ==========")
print(df["director"].value_counts().head(10))

print("\n========== TOP 10 COUNTRIES ==========")
print(df["country"].value_counts().head(10))

print("\n========== TOP 10 GENRES ==========")
print(df["listed_in"].value_counts().head(10))

print("\n========== CONTENT RELEASED PER YEAR ==========")
print(df["release_year"].value_counts().sort_index())

print("\n========== CONTENT ADDED TO NETFLIX PER YEAR ==========")
print(df["added_year"].value_counts().sort_index())

oldest = df[df["release_year"] == df["release_year"].min()]
newest = df[df["release_year"] == df["release_year"].max()]

print("\n========== OLDEST TITLES ==========")
print(oldest[["title", "release_year", "type"]])

print("\n========== NEWEST TITLES ==========")
print(newest[["title", "release_year", "type"]])

print(f"\nAverage Release Year : {df['release_year'].mean():.2f}")

print(
    f"Year with Most Releases : "
    f"{df['release_year'].value_counts().idxmax()}"
)

# ==========================================
# Step 4: Visualizations
# ==========================================

# Movies vs TV Shows
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.savefig(plot_dir / "movies_vs_tvshows.png", dpi=300)
plt.show()

# Rating Distribution
plt.figure(figsize=(12,5))
sns.countplot(
    data=df,
    x="rating",
    order=df["rating"].value_counts().index
)
plt.xticks(rotation=45)
plt.title("Rating Distribution")
plt.tight_layout()
plt.savefig(plot_dir / "rating_distribution.png", dpi=300)
plt.show()

# Top Countries
plt.figure(figsize=(12,6))
sns.countplot(
    data=df,
    x="country",
    order=df["country"].value_counts().head(10).index
)
plt.xticks(rotation=45)
plt.title("Top 10 Countries")
plt.tight_layout()
plt.savefig(plot_dir / "top_countries.png", dpi=300)
plt.show()

# Release Trend
release_trend = (
    df["release_year"]
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12,6))
sns.lineplot(
    x=release_trend.index,
    y=release_trend.values,
    marker="o"
)
plt.title("Netflix Content Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig(plot_dir / "release_trend.png", dpi=300)
plt.show()

# Top Genres
plt.figure(figsize=(12,6))
sns.countplot(
    data=df,
    x="listed_in",
    order=df["listed_in"].value_counts().head(10).index
)
plt.xticks(rotation=45)
plt.title("Top 10 Genres")
plt.tight_layout()
plt.savefig(plot_dir / "top_genres.png", dpi=300)
plt.show()

# Top Directors
plt.figure(figsize=(12,6))
sns.countplot(
    data=df,
    x="director",
    order=df["director"].value_counts().head(10).index
)
plt.xticks(rotation=45)
plt.title("Top 10 Directors")
plt.tight_layout()
plt.savefig(plot_dir / "top_directors.png", dpi=300)
plt.show()

# ==========================================
# Conclusions
# ==========================================

print("\n========== KEY FINDINGS ==========")

print("• Netflix has more Movies than TV Shows.")
print("• TV-14 is the most common content rating.")
print("• The United States contributes the largest catalog.")
print("• Content production increased rapidly after 2015.")
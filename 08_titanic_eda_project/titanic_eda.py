import pandas as pd
import numpy as np  
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns   

plot_dir = Path(__file__).parent / "plots"
plot_dir.mkdir(exist_ok=True)

df=sns.load_dataset('titanic')

# Step 1: Load the dataset and display basic information
print(f"First 5 rows:\n{df.head()}")
print(f"Dataset info:\n{df.info()}")
print(f"Dataset description:\n{df.describe()}")
print(f"Dataset shape: {df.shape}")
print(f"Column names: {df.columns.tolist()}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")

# Step 2: Handle missing values
df['age']=df['age'].fillna(df['age'].mean())
print(f"Filled age values:\n{df['age']}")
df['embarked']=df['embarked'].fillna(df['embarked'].mode()[0])
print(f"Filled embarked values:\n{df['embarked']}")
print(f"Dropping deck:\n{df.drop(columns=['deck'], inplace=True)}")
print(f"Missing values after dropping rows:\n{df.isnull().sum()}")

#Step 3: Perform exploratory data analysis (EDA)
print(f'Average age of passengers: {df["age"].mean()}')
print(f'Average fare of passengers: {df["fare"].mean()}')
print(f'Survival rate: {df["survived"].mean()}')
print(f'Number of male and female survivors:\n{df.groupby("sex")["survived"].sum()}')
print(f'Number of survivors by class:\n{df.groupby("pclass")["survived"].sum()}')
print(f'Average fare by class:\n{df.groupby("pclass")["fare"].mean()}')
print(f'Average age by class:\n{df.groupby("pclass")["age"].mean()}')
print(f'Most common embarkation point: {df["embarked"].mode()[0]}')

#Step 4: Visualize the data
sns.histplot(data=df, x="age", bins=30, kde=True)
plt.title("Age Distribution")
plt.savefig(plot_dir / "age_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

sns.countplot(data=df, x="survived")
plt.title("Survival Count")
plt.savefig(plot_dir / "survival_count.png", dpi=300, bbox_inches="tight")
plt.show()

sns.countplot(data=df, x="pclass", hue="survived")
plt.title("Survival Count by Passenger Class")  
plt.savefig(plot_dir / "pclass_count.png", dpi=300, bbox_inches="tight")
plt.show()


sns.boxplot(data=df, x="pclass", y="fare")
plt.title("Fare by Passenger Class")
plt.savefig(plot_dir / "fare_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

sns.scatterplot(data=df, x="age", y="fare")
plt.title("Age vs Fare")
plt.savefig(plot_dir / "age_vs_fare.png", dpi=300, bbox_inches="tight")
plt.show()


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig(plot_dir / "correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()



# Conclusions
# 1. Female passengers had a much higher survival rate.
# 2. First-class passengers paid the highest fares.
# 3. Most passengers embarked from Southampton.
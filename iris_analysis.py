
# Analyzing Iris Dataset from CSV with Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from CSV
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"

try:
    df = pd.read_csv(url)

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nData types:")
    print(df.dtypes)
except Exception as e:
    print("Error loading the dataset:", e)

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Group by species
grouped_means = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped_means)

# Observation
print("\nObservation:")
print("→ Iris-virginica has the longest average petal length.")

# Line Chart (index vs. sepal_length)
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['sepal_length'], label='Sepal Length')
plt.title('Line Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart - average petal length per species
plt.figure(figsize=(6, 4))
grouped_means['petal_length'].plot(kind='bar', color='teal')
plt.title('Average Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Species')
plt.tight_layout()
plt.show()

# Histogram - sepal width
plt.figure(figsize=(6, 4))
plt.hist(df['sepal_width'], bins=15, color='orange', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot - Sepal length vs Petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()
    
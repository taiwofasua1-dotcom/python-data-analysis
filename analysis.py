import pandas as pd
import matplotlib.pyplot as plt

# Load public dataset: Restaurant tips
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Q1: Does total bill affect tip?
print("\nAverage tip by day:")
print(df.groupby("day")["tip"].mean())

# Q2: Do smokers tip differently?
print("\nAverage tip by smoker:")
print(df.groupby("smoker")["tip"].mean())

# Q3: Tip by time (Lunch vs Dinner)
print("\nAverage tip by time:")
print(df.groupby("time")["tip"].mean())

# Simple chart
df.groupby("day")["tip"].mean().plot(kind="bar", title="Average Tip by Day")
plt.ylabel("Average Tip ($)")
plt.tight_layout()
plt.savefig("avg_tip_by_day.png")
print("\nChart saved as avg_tip_by_day.png")

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("2.csv")

# Line Plot
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="month", y="sales", hue="product", marker="o")
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.grid(True)
plt.show()
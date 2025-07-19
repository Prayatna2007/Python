import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('temperature_data.csv')

# Pivot for heatmap (updated syntax)
heatmap_data = df.pivot(index="month", columns="city", values="temperature")

# Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Average Monthly Temperature (°F)")
plt.xlabel("City")
plt.ylabel("Month")
plt.show()
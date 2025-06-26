import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('1.csv')  #reading csv file

# Plotting
plt.figure(figsize=(10, 6))

# Line plot for Revenue and Expenses
plt.plot(df['Month'], df['Revenue'], label='Revenue', marker='o')
plt.plot(df['Month'], df['Expenses'], label='Expenses', marker='o')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Monthly Revenue vs Expenses')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# Bar plot for Profit
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Profit'], color='green')
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.title('Monthly Profit')
plt.xticks(rotation=45)
plt.show()

# Scatter plot for Visitors vs Revenue
plt.figure(figsize=(10, 6))
plt.scatter(df['Visitors'], df['Revenue'], color='purple')
plt.xlabel('Visitors')
plt.ylabel('Revenue ($)')
plt.title('Visitors vs Revenue')
plt.grid(True)
plt.show()
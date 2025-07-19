import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data from the CSV (embedded directly in the code)
df=pd.read_csv("popn_data.csv")

# Convert population numbers to millions for better readability
df['total_population'] = df['total_population'] / 1e6
df['child_0_14'] = df['child_0_14'] / 1e6
df['adult_15_64'] = df['adult_15_64'] / 1e6
df['aged_65_plus'] = df['aged_65_plus'] / 1e6

# Create the visualization
plt.figure(figsize=(14, 8))

# Plot 1: Total Population Over Time
plt.subplot(2, 2, 1)
plt.plot(df['year'], df['total_population'], 'b-o', linewidth=2, markersize=5)
plt.title('Total Population of Nepal (1950-2050)')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.grid(True, alpha=0.3)

# Plot 2: Population by Age Groups Over Time
plt.subplot(2, 2, 2)
plt.plot(df['year'], df['child_0_14'], 'g-', label='Children (0-14)')
plt.plot(df['year'], df['adult_15_64'], 'b-', label='Adults (15-64)')
plt.plot(df['year'], df['aged_65_plus'], 'r-', label='Aged (65+)')
plt.title('Population by Age Groups')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 3: Population Distribution in Selected Years
years_to_show = [1950, 1980, 2000, 2020, 2050]
selected_data = df[df['year'].isin(years_to_show)]

plt.subplot(2, 2, 3)
bar_width = 0.2
index = np.arange(len(years_to_show))

plt.bar(index, selected_data['child_0_14'], bar_width, label='Children')
plt.bar(index + bar_width, selected_data['adult_15_64'], bar_width, label='Adults')
plt.bar(index + 2*bar_width, selected_data['aged_65_plus'], bar_width, label='Aged')

plt.title('Population Distribution in Key Years')
plt.xlabel('Year')
plt.ylabel('Population (Millions)')
plt.xticks(index + bar_width, years_to_show)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 4: Percentage Composition Over Time
df['child_pct'] = df['child_0_14'] / df['total_population'] * 100
df['adult_pct'] = df['adult_15_64'] / df['total_population'] * 100
df['aged_pct'] = df['aged_65_plus'] / df['total_population'] * 100

plt.subplot(2, 2, 4)
plt.stackplot(df['year'], df['child_pct'], df['adult_pct'], df['aged_pct'], 
              labels=['Children %', 'Adults %', 'Aged %'], 
              colors=['#a6cee3','#1f78b4','#b2df8a'])
plt.title('Age Group Percentage Composition')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
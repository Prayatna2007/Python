import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("employee_salaries.csv")

# Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="department", y="salary")
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary ($)")
plt.show()
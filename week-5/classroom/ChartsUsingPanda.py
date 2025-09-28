import pandas as pd
import matplotlib.pyplot as plt

data = {'Module': ['AI', 'ML', 'Python', 'DataStructures'], 'Teamsize': [135, 125, 125, 115]}
df = pd.DataFrame(data)

df.set_index('Module', inplace=True)
df.plot.pie(y='Teamsize', autopct='%1.1f%%', startangle=130, figsize=(8, 8), title='Team Size Distribution by Module')


#-----------------------------------------------------------------------    
data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Week1": [1000, 2000, 3000, 5000, 7000, 8000, 6700],
    "Week2": [4000, 5000, 2500, 4500, 3500, 5000, 5600],
    "Week3": [5000, 6000, 4500, 3500, 2000, 6000, 4800],
    "Week4": [6000, 5000, 2900, 4500, 3500, 4500, 4500]
}

#----------------------------------------
# df = pd.DataFrame(data)
# df.set_index('Day', inplace=True)

# df.plot.line(marker='o', linewidth=2, title='Line Chart - Weekly Trends')
# plt.show()
#----------------------------------------

# Create DataFrame and set index
df = pd.DataFrame(data)
df.set_index('Day', inplace=True)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Line Chart
df.plot.line(ax=axes[0, 0], marker='o', linewidth=2, title='Line Chart')
axes[0, 0].grid(True, alpha=0.3)

# Bar Chart
df.plot.bar(ax=axes[0, 1], title='Bar Chart')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(True, alpha=0.3, axis='y')

# Histogram
df.plot.hist(ax=axes[1, 0], bins=10, alpha=0.7, title='Histogram', grid=False)
axes[1, 0].grid(True, alpha=0.3)

# Area Chart
df.plot.area(ax=axes[1, 1], alpha=0.7, title='Area Chart')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
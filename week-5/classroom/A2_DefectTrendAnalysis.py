import matplotlib.pyplot as plt

weeks = [1, 2, 3, 4, 5, 6]
defects = [5, 8, 6, 10, 7, 4]

plt.plot(weeks, defects, 
         marker='p', 
         linestyle='dashed', 
         markersize=8, 
         markerfacecolor='red', 
         markeredgecolor='yellow', 
         markeredgewidth=2)

plt.title('Defect Trend Over Time')
plt.xlabel('Week Number')
plt.ylabel('Number of Defects')

plt.grid(True)
plt.savefig('test_results.png') 

plt.show()
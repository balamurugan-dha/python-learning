import matplotlib.pyplot as plt

passed = 45
failed = 10
skipped = 5

test_status = ['Passed', 'Failed', 'Skipped']
test_counts = [passed, failed, skipped]

plt.bar(test_status, test_counts, 
        color=['green', 'red', 'orange'],
        edgecolor='black',                 
        linewidth=1,            
        alpha=1.0)    

plt.title('Test Execution Results', fontsize=14, fontweight='bold')
plt.xlabel('Test Status', fontsize=12)
plt.ylabel('Number of Test Cases', fontsize=12)

plt.show()
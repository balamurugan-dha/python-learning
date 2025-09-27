import matplotlib.pyplot as plt

high = 10
medium = 15
low = 5

defect_counts = [high, medium, low]
severity_labels = ["High", "Medium", "Low"]

plt.pie(defect_counts, 
        labels=severity_labels, 
        autopct='%1.1f%%')

plt.title("Defect Distribution by Severity")

plt.show()
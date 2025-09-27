import pandas as pd
import numpy as np

test_cases = np.array(['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6'])
modules = np.array(['Login', 'Login', 'Payment', 'Payment', 'Reports', 'Reports'])
statuses = np.array(['Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed'])
durations = np.array([12, 15, 20, 18, 25, 22])
data = pd.DataFrame({'TestCase': test_cases, 'Module': modules, 'Status': statuses, 'Duration': durations})
df = pd.DataFrame(data)
print("\n", df)

status_counts = df.groupby("Status")["TestCase"].count()
print("\nTest Case Count by Status:", status_counts)

module_avg_duration = df.groupby("Module")["Duration"].mean()
print("\nAverage Duration per Module:", module_avg_duration)
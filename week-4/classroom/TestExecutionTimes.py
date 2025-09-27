import pandas as pd

execution_times = [12, 15, 20, 18, 25, 30, 22]
labels = ['TC1', 'TC2', 'TC3', 'TC4', 'TC5', 'TC6', 'TC7']

test_series = pd.Series(execution_times, index=labels)
print("\nTest Execution Times Series:\n", test_series)
print("\nFirst 3 test times: ", test_series.head(3))

mean_time = test_series.mean()
print(f"\nMean execution time: {mean_time}")

second_test = test_series.iloc[1]
print(f"\nSecond test time (using iloc): {second_test}")

tc3_time = test_series.loc['TC3']
print(f"\nTC3 execution time (using loc): {tc3_time}")
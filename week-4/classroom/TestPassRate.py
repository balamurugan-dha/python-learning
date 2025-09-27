import pandas as pd

pass_rates = [80, 85, 78, 90, 88]
builds = ['B1', 'B2', 'B3', 'B4', 'B5']

pass_rate_series = pd.Series(pass_rates, index=builds)
print("Test Pass Percentage Across Builds:\n", pass_rate_series)

average_pass_rate = pass_rate_series.mean()
print(f"Average pass rate: {average_pass_rate:}")

highest_build = pass_rate_series.idxmax()
highest_rate = pass_rate_series.max()
print(f"Build with highest pass rate: {highest_build} -> {highest_rate}")

last_build_rate = pass_rate_series.iloc[-1]
print(f"Pass rate of the last build: {last_build_rate}")

b3_rate = pass_rate_series.loc['B3']
print(f"Pass rate of Build B3: {b3_rate}")

normalized_rates = pass_rate_series - pass_rate_series.mean()
print("Normalized pass rates (deviation from average):")
print(normalized_rates)
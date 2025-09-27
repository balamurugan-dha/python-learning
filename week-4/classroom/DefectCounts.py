import pandas as pd

defect_counts = [5, 8, 3, 6, 10, 2, 7]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

defect_series = pd.Series(defect_counts, index=days)
print("Defects Logged Per Day:\n",defect_series)

max_defects = defect_series.max()
print(f"Maximum defects logged in a single day: {max_defects}")

min_day = defect_series.idxmin()
min_defects = defect_series.min()
print(f"Day with minimum defects: {min_day} ({min_defects} defects)")

day5_defects = defect_series.iloc[4]
print(f"Defect count on Day5: {day5_defects}")

wed_defects = defect_series.loc['Wed']
print(f"Defect count on Wednesday: {wed_defects}")

total_defects = defect_series.sum()
print(f"Total defects logged in the week: {total_defects}")
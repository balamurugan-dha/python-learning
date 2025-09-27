import pandas as pd
import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([30, 40, 50])
df = pd.DataFrame([array1, array2], columns=['A', 'B', 'C'])
print("\nDataFrame with rows and columns:\n", df)

series1 = pd.Series([100, 200, 300])
series2 = pd.Series([400, 500, 600])
df2 = pd.DataFrame([series1.values, series2.values], columns=['A', 'B', 'C'])
print("DataFrame with Series as rows:\n", df2)

mani_series = pd.Series([10, 20, 30])
alex_series = pd.Series([20, 30])
mani_values = mani_series.values
alex_values = np.append(alex_series.values, [np.nan])

df3 = pd.DataFrame([mani_values, alex_values], columns=['A', 'B', 'C'],index=['Mani', 'Alex'])
print("DataFrame with Mani and Alex as rows:\n", df3)
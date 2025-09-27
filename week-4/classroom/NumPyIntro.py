import pandas as pd
import numpy as np

execution_times = pd.Series([12, 15, 20, 18, 25, 30, 22])
print("\nOriginal Series:\n", execution_times)
middle_three = execution_times[2:5]
print("\nMiddle three execution times:\n", middle_three)


defects_array = np.array([10, 20, 23, 45, 50])
defects_series = pd.Series(defects_array)
print("\nDefects Series:\n", defects_series)


engineers_data = {
    'Alex': 500,
    'Steve': 200,
    'Bob': 300
}
engineers_series = pd.Series(engineers_data)
print("\nEngineers Series:\n", engineers_series)
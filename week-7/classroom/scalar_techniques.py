import numpy as np
from sklearn.preprocessing import RobustScaler, MinMaxScaler


# Original dataset
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print("Original Data Set: \n", data)


# Robust Scaler
robust_scaler = RobustScaler()
robust_scaled = robust_scaler.fit_transform(data)
print("\nRobustScaler - Scaled Data:\n", robust_scaled)


# Min Max Scaler
minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(data)
print("\nMinMaxScaler - Scaled Data:\n", minmax_scaled)

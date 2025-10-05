import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([[1, 2], [3, 4], [5, 6]])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("Original Data:\n", data)
print("\nScaled Data (StandardScaler):\n", scaled_data)
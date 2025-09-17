import numpy as np

execution_times = np.array([10, 15, 20, 25, 30, 35, 40, 45])
print("Array: ", execution_times)
print("First element: ", execution_times[0])
print("Last element: ", execution_times[-1])
print("Third element: ", execution_times[2])
print("First 3 execution times: ", execution_times[:3])
print("Every alternate execution times", execution_times[::2])

for i, time in enumerate(execution_times, 1):
    print(f"Test {i} execution time: {time} seconds")

reshaped_2darray = execution_times.reshape(2, 4)
print(reshaped_2darray)

execution_times2 = np.array([50, 55, 60, 65])
final_execution_times = np.concatenate([execution_times, execution_times2])
print("Final execution times:", final_execution_times)

# Split into 3 equal parts
split_arrays = np.array_split(final_execution_times, 3)
print("Split array 1:", split_arrays[0])
print("Split array 2:", split_arrays[1])
print("Split array 3:", split_arrays[2])


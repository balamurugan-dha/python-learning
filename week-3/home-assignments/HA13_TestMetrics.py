import numpy as np

execution_data = np.array([
    [7, 49, 30, 29, 17, 20, 33, 36, 31, 48, 15, 25, 38, 42, 19, 45, 28, 22, 35, 40,
     12, 27, 32, 44, 18, 26, 37, 41, 14, 23, 34, 39, 16, 24, 43, 21, 46, 47, 13, 50,
     8, 9, 10, 11, 5, 6, 7, 8, 9, 10],
    [39, 10, 19, 25, 32, 45, 28, 22, 35, 40, 12, 27, 32, 44, 18, 26, 37, 41, 14, 23,
     34, 39, 16, 24, 43, 21, 46, 47, 13, 50, 8, 9, 10, 11, 5, 6, 7, 8, 9, 10, 49, 30,
     29, 17, 20, 33, 36, 31, 48, 15],
    [44, 49, 46, 27, 13, 50, 8, 9, 10, 11, 5, 6, 7, 8, 9, 10, 49, 30, 29, 17, 20, 33,
     36, 31, 48, 15, 25, 38, 42, 19, 45, 28, 22, 35, 40, 12, 27, 32, 44, 18, 26, 37,
     41, 14, 23, 34, 39, 16, 24, 43],
    [35, 30, 20, 11, 10, 49, 30, 29, 17, 20, 33, 36, 31, 48, 15, 25, 38, 42, 19, 45,
     28, 22, 35, 40, 12, 27, 32, 44, 18, 26, 37, 41, 14, 23, 34, 39, 16, 24, 43, 21,
     46, 47, 13, 50, 8, 9, 10, 11, 5, 6],
    [9, 19, 43, 49, 17, 20, 33, 36, 31, 48, 15, 25, 38, 42, 19, 45, 28, 22, 35, 40,
     12, 27, 32, 44, 18, 26, 37, 41, 14, 23, 34, 39, 16, 24, 43, 21, 46, 47, 13, 50,
     8, 9, 10, 11, 5, 6, 7, 8, 9, 10]
])

# 1. Statistical Analysis
cycle_avg = np.mean(execution_data, axis=1)
print("Average execution time per cycle:", cycle_avg)

max_time = np.max(execution_data)
max_indices = np.where(execution_data == max_time)
print(f"Maximum execution time: {max_time} seconds at position Cycle {max_indices[0][0]+1}, Test {max_indices[1][0]+1}")

cycle_std = np.std(execution_data, axis=1)
print("Standard deviation per cycle:", cycle_std)
print()

# 2. Slicing Operations
cycle1_first10 = execution_data[0, :10]
print("First 10 test execution times from Cycle 1:", cycle1_first10)

cycle5_last5 = execution_data[4, -5:]
print("Last 5 test execution times from Cycle 5:", cycle5_last5)

cycle3_alternate = execution_data[2, ::2]
print("Every alternate test from Cycle 3 (first 10):", cycle3_alternate[:10])
print()

# 3. Arithmetic Operations
cycle1_cycle2_add = execution_data[0] + execution_data[1]
print("Cycle 1 + Cycle 2 (first 5):", cycle1_cycle2_add[:5])

cycle1_cycle2_sub = execution_data[0] - execution_data[1]
print("Cycle 1 - Cycle 2 (first 5):", cycle1_cycle2_sub[:5])

cycle4_cycle5_mul = execution_data[3] * execution_data[4]
print("Cycle 4 × Cycle 5 (first 5):", cycle4_cycle5_mul[:5])

cycle4_cycle5_div = execution_data[3] / execution_data[4]
print("Cycle 4 ÷ Cycle 5 (first 5):", cycle4_cycle5_div[:5])
print()

# 4. Power Functions
squared_data = np.power(execution_data, 2)
print("Squared data (first element):", squared_data[0, 0])

cubed_data = np.power(execution_data, 3)
print("Cubed data (first element):", cubed_data[0, 0])

sqrt_data = np.sqrt(execution_data)
print("Square root (first element):", sqrt_data[0, 0])

log_data = np.log(execution_data + 1)
print("Log transformation (first element):", log_data[0, 0])
print()

# 5. Copy Operations
shallow_copy = execution_data.view()
shallow_copy[0, 0] = 999
print("After shallow copy modification - Original[0,0]:", execution_data[0, 0])

deep_copy = execution_data.copy()
deep_copy[0, 0] = 888
print("After deep copy modification - Original[0,0]:", execution_data[0, 0])
print()

# 6. Filtering with Conditions
cycle2_slow_tests = execution_data[1][execution_data[1] > 30]
print("Cycle 2 tests > 30 seconds:", cycle2_slow_tests)
print("Number of slow tests in Cycle 2:", len(cycle2_slow_tests))

consistent_slow_tests = np.all(execution_data > 25, axis=0)
consistent_slow_indices = np.where(consistent_slow_tests)[0]
print("Tests consistently > 25 seconds in all cycles:", consistent_slow_indices + 1)

thresholded_data = execution_data.copy()
thresholded_data[thresholded_data < 10] = 10
print("Minimum value after thresholding:", np.min(thresholded_data))
print("Number of values replaced:", np.sum(execution_data < 10))
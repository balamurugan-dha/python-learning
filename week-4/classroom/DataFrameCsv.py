import pandas as pd

# 1. Create DataFrame
test_data = {
    'TestCase': ['TC1', 'TC2', 'TC3', 'TC4', 'TC5'],
    'Status': ['Passed', 'Failed', 'Passed', 'Failed', 'Passed'],
    'Duration': [12, 15, 20, 18, 25]
}
df = pd.DataFrame(test_data)
print("\nTest Results DataFrame:\n", df.to_string(index=False))


print("\nStatus Column:\n", df['Status'].to_string(index=False))

failed_tests = df[df['Status'] == 'Failed']
print("\nFailed Test Cases:\n", failed_tests.to_string(index=False))

df.to_csv("test_results.csv", header=True, index=True)
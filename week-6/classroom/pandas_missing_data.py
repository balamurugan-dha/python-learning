import pandas as pd

def handle_missing_data():
    df = pd.read_csv("test_results_missing.csv")
    
    print("-------------------------------------------------")
    print(df)
    print("-------------------------------------------------")
    
    missing_counts = df.isnull().sum()
    print(missing_counts)
    print(f"\nTotal missing values: {missing_counts.sum()}")
    
    duration_mean = df['Duration'].mean()
    print(f"Mean Duration: {duration_mean:.2f}")
    
    # Fixed syntax to avoid warnings
    df = df.fillna({'Duration': duration_mean, 'Status': 'Unknown'})
    
    print("-------------------------------------------------")
    print("Data after filling missing values:")
    print(df)
    print("-------------------------------------------------")
    
    rows_before = len(df)
    df = df.dropna()  # Alternative to inplace=True
    rows_after = len(df)
    
    print("Cleaned Data:")
    print(df)
    print("-------------------------------------------------")
    print(f"\nRows removed: {rows_before - rows_after}")
    
    print("\nMissing value count:")
    final_missing = df.isnull().sum()
    print(final_missing)
    print(f"Total missing values: {final_missing.sum()}")

if __name__ == "__main__":
    handle_missing_data()
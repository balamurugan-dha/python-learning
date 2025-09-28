import pandas as pd

def main():
    df = pd.read_csv("variate-analysis-input.csv")
    
    
    # univariate
    print("----------------------------------------------------")
    print(df['Duration'].describe())
    print(f"\nMean of Duration: {df['Duration'].mean()}")
    print(f"Median of Duration: {df['Duration'].median()}")
    print(f"Standard Deviation of Duration: {df['Duration'].std()}")
    print("----------------------------------------------------")

    
    # bivariate
    average_duration_by_status = df.groupby("Status")["Duration"].mean()
    print("Average Duration by Status:")
    print(average_duration_by_status)
    print("----------------------------------------------------")
    

    # multivariate
    defects_by_module_status = df.groupby(["Module","Status"])["Defects"].sum()
    print("Total Defects by Module and Status:")
    print(defects_by_module_status)
    print("----------------------------------------------------")



if __name__ == "__main__":
    main()
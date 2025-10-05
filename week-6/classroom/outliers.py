import pandas as pd



df = pd.read_csv('SalesDataset5Oct.csv')


# IQR method
def detect_outliers_iqr(df, columns):
    outliers_mask = pd.Series([False] * len(df))
    
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        print(f"\n{col}:")
        print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
        print(f"Bounds: [{lower_bound}, {upper_bound}]")
        
        col_outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
        print(f"Number of outliers in {col}: {col_outliers.sum()}")
        
        outliers_mask = outliers_mask | col_outliers
    
    return outliers_mask

numerical_columns = ['Quantity', 'Price per Unit', 'Total Amount']
outliers_mask = detect_outliers_iqr(df, numerical_columns)

print(f"\nTotal records with outliers: {outliers_mask.sum()}")
print(f"Percentage of outliers: {(outliers_mask.sum() / len(df) * 100):.2f}%")

# Create outliers dataset
outliers_df = df[outliers_mask].copy()
outliers_df.to_csv('outliers.csv', index=False)

cleaned_df = df[~outliers_mask].copy()
cleaned_df.to_csv('cleaned_data.csv', index=False)
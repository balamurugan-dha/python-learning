import pandas as pd



df = pd.read_csv('SalesDataset.csv')


percentile_25 = df['Total Amount'].quantile(0.25)
print(f"1. 25th percentile of Total Amount: {percentile_25}")

median_total = df['Total Amount'].median()
print(f"2. Median (50th percentile) of Total Amount: {median_total}")

percentile_75 = df['Total Amount'].quantile(0.75)
print(f"3. 75th percentile of Total Amount: {percentile_75}")

variance_total_amount = df['Total Amount'].var()
print(f"4. Variance in Total Amount: {variance_total_amount:.2f}")

variance_quantity = df['Quantity'].var()
print(f"5. Variance in Quantity: {variance_quantity:.2f}")

correlation_age_total = df['Age'].corr(df['Total Amount'])
print(f"6. Correlation between Age and Total Amount: {correlation_age_total:.4f}")

correlation_quantity_total = df['Quantity'].corr(df['Total Amount'])
print(f"7. Correlation between Quantity and Total Amount: {correlation_quantity_total:.4f}")

correlation_price_total = df['Price per Unit'].corr(df['Total Amount'])
print(f"8. Correlation between Price per Unit and Total Amount: {correlation_price_total:.4f}")
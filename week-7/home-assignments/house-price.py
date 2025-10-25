import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the Dataset
df = pd.read_csv('house_price_regression_dataset.csv')
df = df[['Square_Footage', 'House_Price']]  # Keep only required columns

# 2. Exploratory Data Analysis (EDA)
print("First few rows of the dataset:")
print(df.head())
print("\nDataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Square_Footage'], df['House_Price'], alpha=0.6)
plt.title('Relationship between Square Footage and House Price')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.grid(True)
plt.show()

# 3. Feature and Target Selection
X = df[['Square_Footage']]
y = df['House_Price']

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Building
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nIntercept (b₀): {model.intercept_:.2f}")
print(f"Coefficient (b₁): {model.coef_[0]:.2f}")

# 6. Prediction and Evaluation
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# 7. Visualization
# Regression line plot
plt.figure(figsize=(12, 5))

# Plot 1: Regression line with actual data
plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, alpha=0.6, label='Actual Prices')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.title('Regression Line vs Actual Data')
plt.xlabel('Square Footage')
plt.ylabel('House Price')
plt.legend()
plt.grid(True)

# Plot 2: Actual vs Predicted prices
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.grid(True)

plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt



df = pd.read_csv('salary.csv')
X = df[['YearsExperience']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Linear Regression Results:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.4f}")


print("\nTest Predictions:")
for i, (actual, predicted) in enumerate(zip(y_test, y_pred)):
    print(f"Sample {i+1}: Actual = ${actual:.2f}, Predicted = ${predicted:.2f}")


# show plot

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.7, label='Data Points')

x_line = np.linspace(X['YearsExperience'].min(), X['YearsExperience'].max(), 100)
y_line = model.coef_[0] * x_line + model.intercept_
plt.plot(x_line, y_line, color='red', linewidth=2, label='Regression Line')

plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.title('Salary vs Experience - Linear Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# We are not importing train_test_split because the dataset is too small.

#1. Load Dataset

data_dict = {
    'x1': [1, 2, 3],
    'x2': [2, 1, 4],
    'Output': [6, 8, 14]  # 'y' is our 'Output' column
}
data = pd.DataFrame(data_dict)


# 2. Define X and y
X = data[['x1', 'x2']]  # Independent variables (now two features)
y = data['Output']      # Dependent variable

# 3. Train/Test Split
X_train = X
X_test = X
y_train = y
y_test = y

# 4. Create and Fit the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Print the coefficients to match our earlier result
print("--- Model Coefficients ---")
print(f"Intercept (β0): {model.intercept_:.1f}")
print(f"Coefficients (β1, β2): {model.coef_}")
print(f"Model Equation: y = {model.intercept_:.1f} + {model.coef_[0]:.1f}*x1 + {model.coef_[1]:.1f}*x2\n")

# 5. Make Predictions
y_pred = model.predict(X_test)

#  6. Performance Evaluation
# Because we trained and tested on the same (perfectly fittable) data,
# the error will be zero and R² will be 1.
print("--- Model Performance Evaluation ---")
print(f"Predicted values: {y_pred}")
print(f"Actual values:    {y_test.values}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}") #This is more interpretable
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

# 7. Graph Plotting
# Since we have 2 independent variables (x1, x2), we can't use a 2D plot.
# We must use a 3D plot to visualize the data points and the regression "plane".

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the actual data points
ax.scatter(X_test['x1'], X_test['x2'], y_test, color='blue', s=100, label='Actual Data Points')

# Create a meshgrid to plot the regression plane
# We create a grid of x1 and x2 values
x1_surf = np.linspace(X['x1'].min(), X['x1'].max(), 10)  # creates 10 linear points from min to max
x2_surf = np.linspace(X['x2'].min(), X['x2'].max(), 10)
x1_surf, x2_surf = np.meshgrid(x1_surf, x2_surf)

# Predict 'y' for each point on the grid using the model
# (This is the equation of the plane)
y_plane = model.predict(pd.DataFrame({'x1': x1_surf.ravel(), 'x2': x2_surf.ravel()}))
y_plane = y_plane.reshape(x1_surf.shape)

# Plot the regression plane
ax.plot_surface(x1_surf, x2_surf, y_plane, color='red', alpha=0.3, label='Predicted Plane')

ax.set_xlabel('x1 (Total Years of Experience - equivalent)')
ax.set_ylabel('x2 (Rating)')
ax.set_zlabel('Salary')
ax.set_title('Salary Prediction (3D Regression Plane)')
ax.legend()

plt.show()
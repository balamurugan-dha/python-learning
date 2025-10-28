import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class SalaryPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False
        self.X = None
        self.y = None
        self.data = None
        

    def load_and_train(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            
            self.X = self.data[['YearsExperience', 'Rating']]  # Independent
            self.y = self.data['Salary']                       # Dependent
            self.model.fit(self.X, self.y)
            self.is_trained = True
            
            # model details
            print(f"Intercept (β0): {self.model.intercept_:.2f}")
            print(f"Coefficients: YearsExperience (β1): {self.model.coef_[0]:.2f}, Rating (β2): {self.model.coef_[1]:.2f}")
            print(f"Model Equation: Salary = {self.model.intercept_:.2f} + {self.model.coef_[0]:.2f} * YearsExperience + {self.model.coef_[1]:.2f} * Rating\n")
            
            # predictions on training data
            y_pred = self.model.predict(self.X)
            
            # model performance metrics
            print(f"Mean Squared Error: {mean_squared_error(self.y, y_pred):.2f}")
            print(f"R² Score: {r2_score(self.y, y_pred):.2f}")
            print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(self.y, y_pred)):.2f}")
            return True
            
        except Exception as e:
            print(f"Error loading or training model: {e}")
            return False
    
    def predict_salary(self, years_experience, rating):
        if not self.is_trained:
            print("Model not trained yet. Please call load_and_train() first.")
            return None
        
        try:
            input_data = pd.DataFrame({
                'YearsExperience': [years_experience],
                'Rating': [rating]
            })
        
            predicted_salary = self.model.predict(input_data)[0]
            return predicted_salary
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None
    

    def plot_3d(self):
        if not self.is_trained:
            print("Model not trained yet. Cannot create plot.")
            return
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Scatter plot of actual data points
        ax.scatter(self.X['YearsExperience'], self.X['Rating'], self.y, color='blue', s=60, label='Actual Data Points', alpha=0.7)
        
        # Create a meshgrid for the regression plane
        x1_range = np.linspace(self.X['YearsExperience'].min(), self.X['YearsExperience'].max(), 20)
        x2_range = np.linspace(self.X['Rating'].min(), self.X['Rating'].max(), 20)
        x1_surf, x2_surf = np.meshgrid(x1_range, x2_range)
        
        # Predict salaries for the meshgrid points
        plane_points = pd.DataFrame({'YearsExperience': x1_surf.ravel(),'Rating': x2_surf.ravel()})
        y_plane = self.model.predict(plane_points)
        y_plane = y_plane.reshape(x1_surf.shape)
        
        # Plot the regression plane
        surf = ax.plot_surface(x1_surf, x2_surf, y_plane, alpha=0.5, color='red', label='Regression Plane')
        
        # Customize the plot
        ax.set_xlabel('Years of Experience', fontsize=12, labelpad=10)
        ax.set_ylabel('Rating', fontsize=12, labelpad=10)
        ax.set_zlabel('Salary ($)', fontsize=12, labelpad=10)
        ax.set_title('Salary Prediction: 3D Regression Plane', fontsize=14, pad=20)
        
        # Add a color bar for the surface
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20, label='Salary ($)')
        
        # Add legend
        ax.legend()
        
        # Adjust viewing angle for better perspective
        ax.view_init(elev=20, azim=45)
        
        plt.tight_layout()
        plt.show()
    
    
    def plot_3d_with_prediction(self, pred_experience=None, pred_rating=None, pred_salary=None):
        if not self.is_trained:
            print("Model not trained yet. Cannot create plot.")
            return
        
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Scatter plot of actual data points
        ax.scatter(self.X['YearsExperience'], self.X['Rating'], self.y, color='blue', s=60, label='Actual Data Points', alpha=0.7)
        
        # Highlight prediction point if provided
        if pred_experience is not None and pred_rating is not None and pred_salary is not None:
            ax.scatter([pred_experience], [pred_rating], [pred_salary], 
                      color='green', s=150, marker='*', 
                      label=f'Prediction: {pred_experience} yrs, Rating {pred_rating}', 
                      edgecolors='black', linewidth=2)
        
        # Create a meshgrid for the regression plane
        x1_range = np.linspace(self.X['YearsExperience'].min(), self.X['YearsExperience'].max(), 20)
        x2_range = np.linspace(self.X['Rating'].min(), self.X['Rating'].max(), 20)
        x1_surf, x2_surf = np.meshgrid(x1_range, x2_range)
        
        # Predict salaries for the meshgrid points
        plane_points = pd.DataFrame({'YearsExperience': x1_surf.ravel(),'Rating': x2_surf.ravel()})
        y_plane = self.model.predict(plane_points)
        y_plane = y_plane.reshape(x1_surf.shape)
        
        # Plot the regression plane
        surf = ax.plot_surface(x1_surf, x2_surf, y_plane, alpha=0.4, cmap='viridis', label='Regression Plane')
        
        # Customize the plot
        ax.set_xlabel('Years of Experience', fontsize=12, labelpad=10)
        ax.set_ylabel('Rating', fontsize=12, labelpad=10)
        ax.set_zlabel('Salary ($)', fontsize=12, labelpad=10)
        
        title = 'Salary Prediction: 3D Regression Plane'
        if pred_experience is not None:
            title += f'\nPredicted: ${pred_salary:,.2f} for {pred_experience} yrs, Rating {pred_rating}'
        ax.set_title(title, fontsize=14, pad=20)
        
        # Add a color bar for the surface
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20, label='Salary ($)')
        
        # Add legend
        ax.legend()
        
        # Adjust viewing angle for better perspective
        ax.view_init(elev=20, azim=45)
        
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    predictor = SalaryPredictor()
    success = predictor.load_and_train('salary_with_rating.csv')
    
    if success:
        predictor.plot_3d()
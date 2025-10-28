import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class SalaryPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.is_trained = False
        
    def load_and_train(self, file_path):

        try:
            data = pd.read_csv(file_path)
            
            X = data[['YearsExperience', 'Rating']]  # Independent
            y = data['Salary']                       # Dependent
            self.model.fit(X, y)
            self.is_trained = True
            
            # model details
            print(f"Intercept (β0): {self.model.intercept_:.2f}")
            print(f"Coefficients: YearsExperience (β1): {self.model.coef_[0]:.2f}, Rating (β2): {self.model.coef_[1]:.2f}")
            print(f"Model Equation: Salary = {self.model.intercept_:.2f} + {self.model.coef_[0]:.2f} * YearsExperience + {self.model.coef_[1]:.2f} * Rating\n")
            
            # predictions on training data
            y_pred = self.model.predict(X)
            
            # model performance metrics
            print(f"Mean Squared Error: {mean_squared_error(y, y_pred):.2f}")
            print(f"R² Score: {r2_score(y, y_pred):.2f}")
            print(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y, y_pred)):.2f}")
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


if __name__ == "__main__":
    predictor = SalaryPredictor()
    success = predictor.load_and_train('salary_with_rating.csv')
    
    if success:
        try:
            user_years = float(input("\nEnter years of experience: "))
            user_rating = int(input("Enter rating (1-3): "))
            user_salary = predictor.predict_salary(user_years, user_rating)
            if user_salary:
                print(f"Predicted Salary: ${user_salary:,.2f}")
        except ValueError:
            print("Please enter valid numbers for years (float) and rating (integer)")
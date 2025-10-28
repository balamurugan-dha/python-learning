import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder


class StudentPerformanceModel:
    def __init__(self):
        self.model = LinearRegression()
        self.label_encoder = LabelEncoder()
        self.feature_names = None
        self.is_trained = False
        

    def load_and_preprocess_data(self, file_path):
        # Load dataset
        self.data = pd.read_csv(file_path)
        print(f"Dataset loaded with {len(self.data)} rows and {len(self.data.columns)} columns")
        
        # Display basic info
        print("\nDataset Info:")
        print(self.data.info())
        print("\nFirst 5 rows:")
        print(self.data.head())
        
        # Check for missing values
        print("\nMissing values:")
        print(self.data.isnull().sum())
        
        return self.data
    


    def preprocess_features(self):
        # Create a copy of the data
        df = self.data.copy()
        
        # Handle categorical variable (Extracurricular Activities)
        df['Extracurricular Activities'] = self.label_encoder.fit_transform(df['Extracurricular Activities'])
        
        # Define features and target
        self.X = df.drop('Performance Index', axis=1)
        self.y = df['Performance Index']
        self.feature_names = self.X.columns.tolist()
        
        print(f"\nFeatures: {self.feature_names}")
        print(f"Target: Performance Index")
        
        return self.X, self.y
    

    def train_test_split(self, test_size=0.2, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state
        )
        
        print(f"\nTraining set: {self.X_train.shape}")
        print(f"Testing set: {self.X_test.shape}")
        
        return self.X_train, self.X_test, self.y_train, self.y_test
    

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)
        self.is_trained = True
        print("\nModel training completed!")
        
        # Display coefficients
        coefficients = pd.DataFrame({
            'Feature': self.feature_names,
            'Coefficient': self.model.coef_
        })
        print("\nModel Coefficients:")
        print(coefficients)
        print(f"\nIntercept: {self.model.intercept_:.4f}")
        

    def evaluate_model(self):
        if not self.is_trained:
            print("Model not trained yet!")
            return
        
        # Make predictions
        y_pred = self.model.predict(self.X_test)
        
        # Calculate metrics
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(self.y_test, y_pred)
        
        print("\nModel Evaluation Metrics:")
        print(f"Mean Squared Error (MSE): {mse:.4f}")
        print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
        print(f"R-squared (R²): {r2:.4f}")
        
        return mse, rmse, r2, y_pred
    

    def predict_performance(self, input_features):
        if not self.is_trained:
            print("Model not trained yet! Please train the model first.")
            return None
        
        try:
            # Convert input to 2D array
            input_array = np.array(input_features).reshape(1, -1)
            
            # Make prediction
            prediction = self.model.predict(input_array)[0]
            
            print(f"\nPredicted Performance Index: {prediction:.2f}")
            return prediction
            
        except Exception as e:
            print(f"Error in prediction: {e}")
            return None
    

    def visualize_results(self, y_pred):
        if not self.is_trained:
            print("Model not trained yet!")
            return
        
        plt.figure(figsize=(18, 5))
        
        # Plot 1: Actual vs Predicted scatter plot
        plt.subplot(1, 3, 1)
        plt.scatter(self.y_test, y_pred, alpha=0.7, color='blue')
        plt.plot([self.y_test.min(), self.y_test.max()], [self.y_test.min(), self.y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual Performance Index')
        plt.ylabel('Predicted Performance Index')
        plt.title('Actual vs Predicted Performance\n(Perfect prediction = red line)')
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Residual plot
        plt.subplot(1, 3, 2)
        residuals = self.y_test - y_pred
        plt.scatter(y_pred, residuals, alpha=0.7, color='green')
        plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
        plt.xlabel('Predicted Values')
        plt.ylabel('Residuals')
        plt.title('Residual Plot\n(Good model = random scatter around zero)')
        plt.grid(True, alpha=0.3)
        
        # Plot 3: Feature importance (using coefficients)
        plt.subplot(1, 3, 3)
        feature_importance = pd.DataFrame({
            'Feature': self.feature_names,
            'Coefficient': np.abs(self.model.coef_)  # Use absolute values for importance
        }).sort_values('Coefficient', ascending=True)
        
        plt.barh(feature_importance['Feature'], feature_importance['Coefficient'])
        plt.xlabel('Absolute Coefficient Value')
        plt.title('Feature Importance\n(Larger absolute value = stronger impact)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Additional: Distribution comparison
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(self.y_test, bins=30, alpha=0.7, label='Actual', color='blue', edgecolor='black')
        plt.hist(y_pred, bins=30, alpha=0.7, label='Predicted', color='red', edgecolor='black')
        plt.xlabel('Performance Index')
        plt.ylabel('Frequency')
        plt.title('Distribution: Actual vs Predicted')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.subplot(1, 2, 2)
        plt.hist(residuals, bins=30, alpha=0.7, color='purple', edgecolor='black')
        plt.xlabel('Residual Values')
        plt.ylabel('Frequency')
        plt.title('Distribution of Residuals\n(Should be normally distributed)')
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

        # Print correlation information
        print("\nFeature Correlations with Performance Index:")
        correlations = []
        for feature in self.feature_names:
            corr = self.X[feature].corr(self.y)
            correlations.append((feature, corr))
        
        # Sort by absolute correlation
        correlations.sort(key=lambda x: abs(x[1]), reverse=True)
        for feature, corr in correlations:
            print(f"{feature:35} | Correlation: {corr:7.3f}")



def main():
    # Initialize the model
    student_model = StudentPerformanceModel()
    
    # Load and preprocess data
    data = student_model.load_and_preprocess_data('Student_Performance.csv')
    
    # Preprocess features
    X, y = student_model.preprocess_features()
    
    # Split data
    X_train, X_test, y_train, y_test = student_model.train_test_split()
    
    # Train model
    student_model.train_model()
    
    # Evaluate model
    mse, rmse, r2, y_pred = student_model.evaluate_model()
    
    # Visualize results
    student_model.visualize_results(y_pred)
    
    # 7. User Input Prediction
    print("\n" + "="*50)
    print("USER INPUT PREDICTION")
    print("="*50)
    
    # Get user input for prediction
    print(f"\nPlease enter values for the following features:")
    print("Features available:", student_model.feature_names)
    
    try:
        # Collect user input
        user_input = []
        for feature in student_model.feature_names:
            if feature == 'Extracurricular Activities':
                value = input(f"Enter {feature} (Yes/No): ").strip().capitalize()
                # Convert to numerical (Yes=1, No=0)
                value = 1 if value == 'Yes' else 0
            else:
                value = float(input(f"Enter {feature}: "))
            user_input.append(value)
        
        print(f"\nUser input: {dict(zip(student_model.feature_names, user_input))}")
        
        # Make prediction
        predicted_performance = student_model.predict_performance(user_input)
        
        if predicted_performance is not None:
            print(f"\nBased on the input values, the predicted student performance index is: {predicted_performance:.2f}")
            
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Error: {e}")




if __name__ == "__main__":
    main()
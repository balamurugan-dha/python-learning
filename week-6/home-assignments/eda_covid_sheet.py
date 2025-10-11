import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class CovidEDA:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df = self.df[['Confirmed', 'New cases']]
        self.df_cleaned = None
        self.df_normalized = None
    
    def compute_statistics(self):
        print("Statistical Measures:")
        print(f"Mean - Confirmed: {self.df['Confirmed'].mean():.2f}, New cases: {self.df['New cases'].mean():.2f}")
        print(f"Median - Confirmed: {self.df['Confirmed'].median():.2f}, New cases: {self.df['New cases'].median():.2f}")
        print(f"Variance - Confirmed: {self.df['Confirmed'].var():.2f}, New cases: {self.df['New cases'].var():.2f}")
        print(f"Standard Deviation - Confirmed: {self.df['Confirmed'].std():.2f}, New cases: {self.df['New cases'].std():.2f}")
        print("\nCorrelation Matrix:")
        print(self.df.corr())
    
    def detect_outliers(self):
        def remove_outliers(column):
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            return self.df[(self.df[column] >= Q1 - 1.5*IQR) & (self.df[column] <= Q3 + 1.5*IQR)]
        
        self.df_cleaned = remove_outliers('Confirmed')
        self.df_cleaned = remove_outliers('New cases')
        print("\nCleaned Dataset (after outlier removal):")
        print(self.df_cleaned.head())
    
    def normalize_data(self):
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(self.df_cleaned)
        self.df_normalized = pd.DataFrame(normalized_data, columns=['Confirmed_normalized', 'New_cases_normalized'])
        print("\nNormalized Data:")
        print(self.df_normalized.head())
    
    def visualize(self):
        # Histograms before normalization
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        self.df['Confirmed'].hist(ax=axes[0,0], bins=30)
        axes[0,0].set_title('Confirmed Cases (Before Normalization)')
        
        self.df['New cases'].hist(ax=axes[0,1], bins=30)
        axes[0,1].set_title('New Cases (Before Normalization)')
        
        # Histograms after normalization
        self.df_normalized['Confirmed_normalized'].hist(ax=axes[1,0], bins=30)
        axes[1,0].set_title('Confirmed Cases (After Normalization)')
        
        self.df_normalized['New_cases_normalized'].hist(ax=axes[1,1], bins=30)
        axes[1,1].set_title('New Cases (After Normalization)')
        
        plt.tight_layout()
        plt.show()
        
        # Heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap: Confirmed vs New Cases')
        plt.show()

# Usage
covid_analysis = CovidEDA('country_wise_latest.csv')
covid_analysis.compute_statistics()
covid_analysis.detect_outliers()
covid_analysis.normalize_data()
covid_analysis.visualize()
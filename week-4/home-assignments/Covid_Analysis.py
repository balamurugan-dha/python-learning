import pandas as pd
import numpy as np


class COVIDDataLoader:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.load_data()
    
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print("\nData loaded successfully!")
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def get_basic_info(self):
        if self.data is not None:
            print(f"Dataset shape: {self.data.shape}")
        else:
            print("No data loaded")



class COVIDAnalyzer(COVIDDataLoader):
    
    def __init__(self, file_path):
        super().__init__(file_path)
    
    def summarize_cases_by_region(self):
        if self.data is not None:
            region_summary = self.data.groupby('Country/Region').agg({
                'Confirmed': 'sum',
                'Deaths': 'sum',
                'Recovered': 'sum'
            }).reset_index()
            print("\n-------------------------------------------------------------------")
            print("\n1. Case Counts by Region:")
            print("\n-------------------------------------------------------------------")
            print(region_summary)
            return region_summary
        return None
    

    def filter_low_cases(self):
        if self.data is not None:
            filtered_data = self.data[self.data['Confirmed'] >= 100]
            print("\n-------------------------------------------------------------------")
            print(f"\n2. Filtered data (Confirmed cases >= 100):")
            print("\n-------------------------------------------------------------------")
            print(f"Original records: {len(self.data)}")
            print(f"Filtered records: {len(filtered_data)}")
            return filtered_data
        return None
    

    def region_highest_confirmed(self):
        if self.data is not None:
            region_totals = self.data.groupby('Country/Region')['Confirmed'].sum()
            highest_region = region_totals.idxmax()
            highest_cases = region_totals.max()
            print("\n-------------------------------------------------------------------")
            print(f"\n3. Region with Highest Confirmed Cases:")
            print("\n-------------------------------------------------------------------")
            print(f"{highest_region}: {highest_cases:,} cases")
            return highest_region, highest_cases
        return None
    

    def sort_by_confirmed_cases(self, output_file='sorted_by_confirmed.csv'):
        if self.data is not None:
            sorted_data = self.data.sort_values('Confirmed', ascending=True)
            sorted_data.to_csv(output_file, index=False)
            print("\n-------------------------------------------------------------------")
            print(f"\n4. Data sorted by confirmed cases and saved to '{output_file}'")
            print("\n-------------------------------------------------------------------")
            print(f"Top 5 sorted countries by confirmed cases:")
            print(sorted_data[['Country/Region', 'Confirmed']].head())
            return sorted_data  
        return None
    

    def top_5_countries(self):
        if self.data is not None:
            top_5 = self.data.nlargest(5, 'Confirmed')[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
            print("\n-------------------------------------------------------------------")
            print("\n5. Top 5 Countries by Confirmed Cases:")
            print("\n-------------------------------------------------------------------")
            print(top_5)
            return top_5
        return None
    

    def region_lowest_deaths(self):
        if self.data is not None:
            region_deaths = self.data.groupby('WHO Region')['Deaths'].sum()
            lowest_region = region_deaths.idxmin()
            lowest_deaths = region_deaths.min()
            print("\n-------------------------------------------------------------------")
            print(f"\n6. Region with Lowest Death Count:")
            print("\n-------------------------------------------------------------------")
            print(f"{lowest_region}: {lowest_deaths:,} deaths")
            return lowest_region, lowest_deaths
        return None
    

    def india_case_summary(self):
        if self.data is not None:
            india_data = self.data[self.data['Country/Region'] == 'India']
            if not india_data.empty:
                print("\n-------------------------------------------------------------------")
                print("\n7. India's Case Summary:")
                print("\n-------------------------------------------------------------------")
                print(india_data[['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active']].iloc[0])
                return india_data.iloc[0]
            else:
                print("India data not found")
                return None
        return None
    

    def calculate_mortality_rate(self):
        if self.data is not None:
            # calculate and add mortality rate column data for each country first
            self.data['Mortality_Rate'] = (self.data['Deaths'] / self.data['Confirmed']) * 100
            
            # group by region and calculate average mortality rate
            region_mortality = self.data.groupby('WHO Region').agg({
                'Mortality_Rate': 'mean',
                'Deaths': 'sum',
                'Confirmed': 'sum'
            })
            region_mortality['Overall_Mortality_Rate'] = (region_mortality['Deaths'] / region_mortality['Confirmed']) * 100
            
            print("\n-------------------------------------------------------------------")
            print("\n8. Mortality Rate by Region:")
            print("\n-------------------------------------------------------------------")
            print(region_mortality[['Mortality_Rate', 'Overall_Mortality_Rate']].round(2))
            return region_mortality
        return None
    

    def compare_recovery_rates(self):
        if self.data is not None:
            # Calculate and add recovery rate for each country first
            self.data['Recovery_Rate'] = (self.data['Recovered'] / self.data['Confirmed']) * 100
            
            # Group by region
            region_recovery = self.data.groupby('WHO Region').agg({
                'Recovery_Rate': 'mean',
                'Recovered': 'sum',
                'Confirmed': 'sum'
            })
            region_recovery['Overall_Recovery_Rate'] = (region_recovery['Recovered'] / region_recovery['Confirmed']) * 100
            
            print("\n-------------------------------------------------------------------")
            print("\n9. Recovery Rates by Region:")
            print("\n-------------------------------------------------------------------")
            print(region_recovery[['Recovery_Rate', 'Overall_Recovery_Rate']].round(2))
            return region_recovery
        return None
    

    def detect_outliers(self):
        if self.data is not None:
            confirmed_cases = self.data['Confirmed']
            mean_cases = confirmed_cases.mean()
            std_cases = confirmed_cases.std()
            
            lower_bound = mean_cases - 2 * std_cases
            upper_bound = mean_cases + 2 * std_cases
            
            outliers = self.data[(self.data['Confirmed'] < lower_bound) | (self.data['Confirmed'] > upper_bound)]
            
            print("\n-------------------------------------------------------------------")
            print(f"\n10. Outliers Detection (Mean: {mean_cases:.0f}, Std: {std_cases:.0f})")
            print("\n-------------------------------------------------------------------")
            print(f"Bounds: Lower = {lower_bound:.2f}, Upper = {upper_bound:.2f}")
            print(f"Number of outliers: {len(outliers)}")
            print("Outlier countries:")
            print(outliers[['Country/Region', 'Confirmed', 'WHO Region']])
            return outliers
        return None
    

    def group_by_country_region(self):
        if self.data is not None:
            grouped_data = self.data.groupby(['WHO Region', 'Country/Region']).agg({
                'Confirmed': 'first',
                'Deaths': 'first',
                'Recovered': 'first'
            })
            print("\n-------------------------------------------------------------------")
            print("\n11. Data grouped by Region and Country:")
            print("\n-------------------------------------------------------------------")
            print(grouped_data)
            return grouped_data
        return None
    
    def regions_zero_recovered(self):
        if self.data is not None:
            # Find countries with zero recovered cases
            zero_recovered_countries = self.data[self.data['Recovered'] == 0]
            
            if not zero_recovered_countries.empty:
                regions_with_zero = zero_recovered_countries['WHO Region'].unique()
                print("\n-------------------------------------------------------------------")
                print("\n12. Regions with countries having zero recovered cases:")
                print("\n-------------------------------------------------------------------")
                print(regions_with_zero)
                print("\nCountries with zero recovered cases:")
                print(zero_recovered_countries[['Country/Region', 'WHO Region', 'Confirmed', 'Recovered']])
                return regions_with_zero, zero_recovered_countries
            else:
                print("No countries with zero recovered cases found")
                return None, None
        return None, None
    

    def run_all_analyses(self):
        print("\n")
        print("********************************")
        print("COVID-19 DATA ANALYSIS REPORT")
        print("********************************")
        
        analyses = [
            self.summarize_cases_by_region,
            self.filter_low_cases,
            self.region_highest_confirmed,
            self.sort_by_confirmed_cases,
            # self.top_5_countries,
            # self.region_lowest_deaths,
            # self.india_case_summary,
            # self.calculate_mortality_rate,
            # self.compare_recovery_rates,
            # self.detect_outliers,
            # self.group_by_country_region,
            # self.regions_zero_recovered
        ]
        print(type(analyses))
        for i, analysis in enumerate(analyses, 1):
            try:
                analysis()
            except Exception as e:
                print(f"Error in analysis {i}: {e}")




# Main execution
if __name__ == "__main__":
    analyzer = COVIDAnalyzer('country_wise_latest.csv')
    
    analyzer.get_basic_info()
    
    analyzer.run_all_analyses()
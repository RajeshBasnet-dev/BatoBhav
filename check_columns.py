import pandas as pd

df = pd.read_csv('dataset/cleaned_nepali_housing_data.csv')
city_columns = [col for col in df.columns if col.startswith('City_')]
print("City Columns:", sorted(city_columns))
print("All Columns:", sorted(df.columns))
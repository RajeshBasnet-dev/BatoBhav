import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('dataset/2020-4-27.csv')

# Function to convert area to square feet
def convert_area(area_str):
    if pd.isna(area_str) or not isinstance(area_str, str):
        return np.nan
    try:
        # Remove extra spaces and normalize
        area_str = area_str.strip()
        
        if 'Aana' in area_str:
            if '-' in area_str:
                parts = area_str.replace(' Aana', '').split('-')
                aana = float(parts[1]) if len(parts) > 1 else 0
            else:
                aana = float(area_str.replace(' Aana', ''))
            return aana * 342.25
        
        elif 'Ropani' in area_str:
            if '-' in area_str:
                ropani = float(area_str.replace(' Ropani', '').split('-')[0])
            else:
                ropani = float(area_str.replace(' Ropani', ''))
            return ropani * 5476
        
        elif 'Sq. Feet' in area_str or 'Sq. Meter' in area_str:
            value = float(area_str.replace(' Sq. Feet', '').replace(' Sq. Meter', ''))
            if 'Sq. Meter' in area_str:
                value *= 10.764
            return value
        
        return np.nan
    except (ValueError, IndexError):
        return np.nan

# Convert Area and Build Area to square feet
df['Area_sqft'] = df['Area'].apply(convert_area)
df['Build Area_sqft'] = df['Build Area'].apply(convert_area)

# Fill missing Area_sqft with Build Area_sqft where available
df['Area_sqft'] = df['Area_sqft'].fillna(df['Build Area_sqft'])

# Handle missing values in Bedroom and Bathroom
df['Bedroom'] = df['Bedroom'].fillna(df['Bedroom'].median()).replace(0, df['Bedroom'].median())
df['Bathroom'] = df['Bathroom'].fillna(df['Bathroom'].median()).replace(0, df['Bathroom'].median())

# Drop rows with missing Price, Area_sqft, or City
df = df.dropna(subset=['Price', 'Area_sqft', 'City'])

# Encode City with One-Hot Encoding
df = pd.get_dummies(df, columns=['City'], prefix='City')

# Select features for model
features = ['Area_sqft', 'Bedroom', 'Bathroom'] + [col for col in df.columns if col.startswith('City_')]
cleaned_df = df[features + ['Price']]

# Save cleaned data
cleaned_df.to_csv('dataset/cleaned_nepali_housing_data.csv', index=False)
print("Cleaned data saved to dataset/cleaned_nepali_housing_data.csv")
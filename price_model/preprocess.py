import pandas as pd

def preprocess_input(area, bedrooms, bathrooms, city):
    city_columns = [
        'City_Bhairahawa', 'City_Bhaktapur', 'City_Biratnagar', 'City_Butwal',
        'City_Chitwan', 'City_Dhading', 'City_Dharan', 'City_Illam',
        'City_Jhapa', 'City_Kapilvastu', 'City_Kaski', 'City_Kathmandu',
        'City_Kavre', 'City_Kirtipur', 'City_Lalitpur', 'City_Mahottari',
        'City_Makwanpur', 'City_Morang', 'City_Nawalparasi', 'City_Nawalpur',
        'City_Parsa', 'City_Pokhara', 'City_Rupandehi', 'City_Surkhet',
        'City_Tanahu'
    ]
    features = {
        'Area_sqft': area,
        'Bedroom': bedrooms,
        'Bathroom': bathrooms
    }
    for city_col in city_columns:
        features[city_col] = 1 if city_col == f'City_{city}' else 0
    input_data = pd.DataFrame(
        [features],
        columns=['Area_sqft', 'Bedroom', 'Bathroom'] + city_columns
    )
    return input_data
import pandas as pd
from matplotlib import pyplot as plt

# Set font to Times New Roman, size 12pt
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# Load data
file_path = 'data/02-YuMing_indexed.csv'
df = pd.read_csv(file_path)
df.set_index('Time', inplace=True)

"""
Standardize latitude and longitude format for easier distance calculations
"""
# Ensure latitude and longitude columns exist
if 'Latitude' in df.columns and 'Longitude' in df.columns:
    # Process latitude: Extract numerical values and set sign based on N/S
    latitude_values = df['Latitude'].str.extract(r'(\d+\.\d+)').astype(float)
    latitude_sign = df['Latitude'].str.contains('N').map({True: 1, False: -1})

    # Check data length
    print(f"Latitude values length: {len(latitude_values)}, Sign length: {len(latitude_sign)}")

    df['Latitude'] = latitude_values[0] * latitude_sign

    # Process longitude: Extract numerical values and set sign based on E/W
    longitude_values = df['Longitude'].str.extract(r'(\d+\.\d+)').astype(float)
    longitude_sign = df['Longitude'].str.contains('E').map({True: 1, False: -1})

    # Check data length
    print(f"Longitude values length: {len(longitude_values)}, Sign length: {len(longitude_sign)}")

    df['Longitude'] = longitude_values[0] * longitude_sign

    # Display processed results
    print(df[['Latitude', 'Longitude']].head())
else:
    print("Missing Latitude or Longitude column in the dataset")

"""
Standardize unit conversions
"""
# Calculate water speed (m/s)
df['WaterSpeed'] = df['ShipSpd'] - df['ShipSpdToWater']
# Convert wind speed to m/s
df['WindSpeed'] = df['WindSpd'] / 3.6
# Convert ship speed to m/s
df['ShipSpeed'] = df['ShipSpd'] * 0.51444
# Convert fuel consumption rate to tons
df['FuelConsumptionRate'] = df['FuelConsumptionRate'] / 1000
# Round values to four decimal places
df = df.round(4)

"""
Filter out abnormal values
"""
# Remove abnormal ship speed values
df = df[(df['ShipSpeed'] >= 3) & (df['ShipSpeed'] <= 8)]
df = df[(df['EngineSpeed'] >= 45) & (df['EngineSpeed'] <= 78)]

"""
Remove unnecessary variables
"""
df = df.drop(columns=['FuelConsumption', 'MEFOInTemp', 'FCMFODensity', 'MESFOC_kw', 'MESFOC_nmile', 'METorque',
                      'MEShaftPow', 'ShipSpdToWater', 'WindSpd', 'ShipSpd', 'ShipHeel', 'ShipSlip'])

"""
Reorder columns
"""
new_order = ['EngineSpeed', 'ShipTrim', 'ShipDraft', 'WindSpeed', 'WindDirection',
             'WaterSpeed', 'FuelConsumptionRate', 'ShipSpeed', 'Latitude', 'Longitude']
df = df.reindex(columns=new_order)

"""
Save the processed final file
"""
print("Data processing completed, containing {0} rows and {1} columns".format(len(df), df.shape[1]))
df.to_csv('data/03-YuMing_final.csv')

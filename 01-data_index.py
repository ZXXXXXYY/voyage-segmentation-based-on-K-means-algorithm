import pandas as pd

# Load CSV file
def load_csv(filename):
    # Use pandas to directly load the CSV file as a DataFrame
    return pd.read_csv(filename)

file_path = 'data/01-YuMing_raw.csv'
df = load_csv(file_path)

# Remove unnecessary columns
df = df.drop(columns=['LogIndex', 'PCDate', 'MEActMGOCons', 'DGActFOCons', 'BlrActFOCons', 'DGActMGOCons',
                      'BlrActMGOCons', 'DGAccFOCons', 'BlrAccFOCons', 'DGAccMGOCons', 'BlrAccMGOCons', 'DGFOInTemp',
                      'BlrFOInTemp', 'DGMGOInTemp', 'BlrMGOInTemp', 'DGFODensity', 'BlrFODensity', 'DGMGODensity',
                      'BlrMGODensity', 'DG1Power', 'DG2Power', 'DG3Power', 'ShipDraughtBow', 'ShipDraughtAstern',
                      'ShipDraughtMidLft', 'ShipDraughtMidRgt'])

# Rename columns for better readability
df = df.rename(columns={'PCTime': 'Time', 'MERpm': 'EngineSpeed', 'WindDir': 'WindDirection',
                        'MEActFOCons': 'FuelConsumptionRate', 'MEAccFOCons': 'FuelConsumption'})

# Standardize time format
df['Time'] = pd.to_datetime(df['Time'], errors='coerce', format='%H:%M:%S')
df.set_index('Time', inplace=True)

# Print dataset summary
print("Data loading completed, containing {0} rows and {1} columns".format(len(df), df.shape[1]))

# Save processed data to a new CSV file
df.to_csv('data/02-YuMing_indexed.csv')

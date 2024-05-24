import pandas as pd
import os

def dataParsing(file_path):
    """Parse the traverse data from a CSV file and return a DataFrame."""
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Traverse data file not found.")

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Validate the data
        required_columns = ['Point', 'Easting', 'Northing']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Traverse data file is missing the following required columns: {', '.join(missing_columns)}")

        # Check for missing values
        if df[['Easting', 'Northing']].isnull().any().any():
            raise ValueError("Traverse data file contains missing values.")

        # Check if the 'Point' column is of integer type
        if df['Point'].dtype != 'int64':
            df['Point'] = df['Point'].astype('int64')

        return df
    except Exception as e:
        raise Exception(f"Error processing traverse data file: {e}")

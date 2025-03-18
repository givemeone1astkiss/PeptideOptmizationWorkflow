import pandas as pd

def read_csv(csv_path):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    csv_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The data from the CSV file as a DataFrame.
    """
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


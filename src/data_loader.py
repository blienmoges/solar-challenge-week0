import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

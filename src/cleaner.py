import pandas as pd

def clean_data(df: pd.DataFrame,remove_column) -> pd.DataFrame:
    #Delete Sales Person
    df = df.drop(columns=[c for c in remove_column if c in df.columns])

    print(df.head())
    return df
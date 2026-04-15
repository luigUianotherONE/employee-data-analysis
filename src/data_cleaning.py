import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df["full_name"] = df["first_name"] + " " + df["last_name"]
    df = df.drop_duplicates()
    df = df.apply(lambda x: x.strip() if isinstance(x, str) else x)
    
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["years_of_experience"] = pd.to_numeric(df["years_of_experience"], errors="coerce")
    
    df = df.dropna()
    return df
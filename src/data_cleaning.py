import pandas as pd

def clean_data(df):
    df = df.copy()

    df.columns = df.columns.str.lower().str.replace(' ', '_')

    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    df["full_name"] = df["first_name"] + " " + df["last_name"]

    df = df.drop_duplicates()

    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["years_of_experience"] = pd.to_numeric(df["years_of_experience"], errors="coerce")

    df = df.dropna(subset=["email", "salary"])

    cols = list(df.columns)
    cols.insert(2, cols.pop(cols.index("full_name")))
    df = df[cols]

    return df


def salary_by_gender(df):
    return df.groupby("gender")["salary"].mean()

def experience_correlation(df):
    return df[["years_of_experience", "salary"]].corr()

def top_earners(df):
    return df.sort_values(by="salary", ascending=False).head(10)
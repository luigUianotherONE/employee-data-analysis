def salary_by_gender(df):
    return df.groupby("gender")["salary"].agg(["mean", "median", "count"])


def salary_by_department(df):
    return df.groupby("department")["salary"].mean().sort_values(ascending=False)


def experience_correlation(df):
    return df[["years_of_experience", "salary"]].corr()


def top_earners(df):
    return df.sort_values(by="salary", ascending=False).head(10)


def salary_distribution(df):
    return df["salary"].describe()

def invalid_phones_summary(df):
    return df["phone_error"].value_counts()


import pandas as pd

# Getting started with data organization
df = pd.read_csv("data\\employees.csv")
try:
    df.to_excel('data\\employees.xlsx',index=False)
except Exception:
    print(f"Something went wrong {Exception}")
else:
    print("Everything is OK")

df = pd.read_excel('data\\employees.xlsx')
print(df.head())

# ----- CHECKING THE DATA -----
# First we'll search for missing values or duplicates in the data.
print(df.isnull().sum())
print(df.duplicated().sum())

# ----- ANALYSING COLUMNS -----
# Now, after analysing the data, we can see that the column names aren't in a good format, 
# so we'll change them to be more readable and easier to work with. 
# We'll convert them to lowercase and replace spaces with underscores.
print(df.columns)
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(df.columns)

# ----- TRANSFORMING THE DATA (NAMES COLUMNS) -----
# If we're searching for a specific employee, would have to search for their first and last name separately, 
# so we'll create a new column that combines the first and last name into a full name column.
df["full_name"] = df["first_name"] + " " + df["last_name"]
full_name_column = df.pop("full_name")
df.insert(2, "full_name", full_name_column)

# ----- VALIDATING THE DATA (EMAILS) -----
# Now let's check out if the email addresses are in a valid format. We can use a simple regex pattern to check for valid email formats.
import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def validate_email(email):
    if not isinstance(email, str):
        return False
    return bool(re.match(pattern, email))
df["email_valid"] = df["email"].apply(validate_email)
print(df[df["email_valid"]])

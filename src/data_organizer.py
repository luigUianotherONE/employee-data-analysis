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
df = df.drop_duplicates()
df = df.apply(lambda x: x.strip() if isinstance(x, str) else x)
print(df)

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

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str):
        return False
    return bool(re.match(pattern, email))

df["email_valid"] = df["email"].apply(validate_email)

valid_email = df[df["email_valid"] == True]
invalid_email = df[df["email_valid"]== False]
total = len(df)
valid = df["email_valid"].sum()
invalid = total - valid

print(f"Total rows: {total}")
print(f"Valid emails: {valid}")
print(f"Invalid emails: {invalid}")

# ----- VALIDATING THE DATA (PHONE NUMBERS) -----

import re

def validate_phone_number(phone):
    """
    Clean + format + validate US phone numbers (E.164)

    Returns:
        formatted_phone (str or None),
        is_valid (bool),
        error_reason (str or None)
    """

    # --- remove extension ---
    if not isinstance(phone, str):
        return None, False, "not_string"
    phone = phone.split('x')[0]

    # --- clean ---
    digits = re.sub(r'\D', '', phone)
    if not digits:
        return None, False, "empty"

    # --- format ---
    if len(digits) == 11 and digits.startswith("1"):
        formatted = "+1" + digits[1:]
    elif len(digits) == 10:
        formatted = "+1" + digits
    else:
        return None, False, "invalid_length"

    # --- validate ---
    if not re.match(r'^\+1\d{10}$', formatted):
        return None, False, "invalid_format"

    return formatted, True, None
df[["phone", "phone_valid", "phone_error"]] = df["phone"].apply(
    lambda x: pd.Series(validate_phone_number(x))
)
print(df)
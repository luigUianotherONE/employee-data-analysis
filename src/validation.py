import re
import pandas as pd


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
    if not isinstance(email, str):
        return False
    return bool(re.match(pattern, email))

def validate_phone_number(phone):
    if pd.isna(phone):
        return None, False, "missing"

    if not isinstance(phone, str):
        return None, False, "not_string"

    phone = phone.split('x')[0]

    digits = re.sub(r'\D', '', phone)
    if not digits:
        return None, False, "empty"

    if len(digits) == 11 and digits.startswith("1"):
        formatted = "+1" + digits[1:]
    elif len(digits) == 10:
        formatted = "+1" + digits
    else:
        return None, False, "invalid_length"

    if not re.match(r'^\+1\d{10}$', formatted):
        return None, False, "invalid_format"

    return str(formatted), True, None

def validate_data(df):
    df = df.copy()

    df["email_valid"] = df["email"].apply(validate_email)

    df["phone_clean"], df["phone_valid"], df["phone_error"] = zip(
        *df["phone"].apply(validate_phone_number)
    )

    return df


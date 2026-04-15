import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not isinstance(email, str):
        return False
    return bool(re.match(pattern, email))

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


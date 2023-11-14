import re
from datetime import datetime


def get_field_type(value):
    if is_email(value):
        return "email"
    elif is_phone(value):
        return "phone"
    elif is_date(value):
        return "date"
    else:
        return "text"


def is_email(value):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, value))


def is_phone(value):
    phone_regex = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
    return bool(re.match(phone_regex, value))


def is_date(value):
    date_formats = ['%d.%m.%Y', '%Y-%m-%d']
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False

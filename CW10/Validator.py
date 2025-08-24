import re


def validator_username(username):

    regex_pattern_username = r"^[a-zA-Z0-9]{6,12}$"
    if re.match(regex_pattern_username, username):
        return True
    return False


def validator_password(password):

    regex_pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    if re.match(regex_pattern_password, password):
        return True
    return False


def validator_email(email):
    regex_pattern_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex_pattern_email, email):
        return True
    return False


def validator_phone(phone):
    regex_pattern_phone = r'^09\d{9}$'
    if re.match(regex_pattern_phone, phone):
        return True
    return False


def validator_date(date):
    regex_pattern_date = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    if not re.match(regex_pattern_date, date):
        return True
    return False

from datetime import datetime
import re


# def validator_username(username):

#     # regex_pattern_username = r'^[a-zA-Z0-9]{6,12}$'
#     # # if re.match(regex_pattern_username, username):
#     # return True
#     # # return False


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


def validate_trip_id(trip_id):
    if not isinstance(trip_id, int) or trip_id <= 0:
        raise ValueError("Trip ID must be a positive number.")
    return True


def validate_city(city):
    if not city or not city.strip():
        raise ValueError("City name cannot be empty.")
    if len(city) < 2:
        raise ValueError(
            "The number of characters for the name must be at least two characters.")
    return True


def validate_origin_destination(origin, destination):
    if origin == destination:
        raise ValueError("Your origin and destination are the same.")
    return True


def validate_trip_times(start_time, end_time):
    try:
        fmt = "%H:%M"
        st = datetime.strptime(start_time, fmt)
        et = datetime.strptime(end_time, fmt)
    except ValueError:
        raise ValueError(
            "The time format is wrong. The correct format is: 12:30")

    if et <= st:
        raise ValueError("The start time is after the end time.")
    return True


def validate_price(price):
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("The cost amount is invalid")
    return True

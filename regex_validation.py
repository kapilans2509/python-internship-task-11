# Task 11: Regular Expressions for Data Validation

import re

# -------- Validation Functions --------

def validate_email(email):
    """
    Validates an email address using regex
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def validate_phone(phone):
    """
    Validates Indian mobile numbers (10 digits, starts with 6-9)
    """
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone)


def validate_password(password):
    """
    Password rules:
    - At least 8 characters
    - At least one digit
    - At least one special character
    """
    pattern = r'^(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password)


# -------- Testing Inputs --------

email = input("Enter email: ")
phone = input("Enter mobile number: ")
password = input("Enter password: ")

print("\n--- Validation Results ---")

if email and validate_email(email):
    print("Email is valid")
else:
    print("Invalid email format")

if phone and validate_phone(phone):
    print("Mobile number is valid")
else:
    print("Invalid mobile number")

if password and validate_password(password):
    print("Password is strong")
else:
    print("Password must be at least 8 characters with digits and special symbols")

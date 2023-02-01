from enum import StrEnum


class UserErrors(StrEnum):
    USERNAME_LENGTH = "Username must be atleast 4 characters"
    USERNAME_AlPHA = "Username must start with an alphabet character"
    PASSWORD_LENGTH = "Password must be atleast 8 characters"
    PASSWORD_ALPHA = "Password must have atleast 2 alphabetic characters"
    PASSWORD_UPPER = "Password must have atleast 1 uppercase letter"
    PASSWORD_LOWER = "Password must have atleast 1 lowercase letter"
    PASSWORD_SIGN = "Password must have atleast one sign character"
    PASSWORD_DIGIT = "Password must have atleast one digit"
    PHONE_LENGTH = 'Phone number must be 11 digits'
    PHONE_TYPE = ' Type of phone number must be a integer'
    PHONE_AlPHA_1 = "Password must start with zero"
    PHONE_AlPHA_2 = "Password second character must be number 9"
    
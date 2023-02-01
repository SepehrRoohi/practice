from .enum import UserErrors


class UsernameLengthError(ValueError):
    
    def __str__(self):
        return UserErrors.USERNAME_LENGTH


class UsernameStartDigitError(ValueError):

    def __str__(self):
        return UserErrors.USERNAME_AlPHA


class PasswordLengthError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_LENGTH


class PasswordAlphabetError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_ALPHA


class PasswordUpperCaseError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_UPPER


class PasswordLowerCaseError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_LOWER


class PasswordSignError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_SIGN


class PasswordDigitError(ValueError):

    def __str__(self):
        return UserErrors.PASSWORD_DIGIT

class PhoneTypeError(ValueError):
    
    def __str__(self):
        return  UserErrors.PHONE_TYPE

class PhoneLengthError(ValueError):
    
    def __str__(self):
        return UserErrors.PHONE_LENGTH
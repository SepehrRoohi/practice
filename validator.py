from helper.exception import(
    UsernameLengthError,
    UsernameStartDigitError
)
class UserValidator():

    def __init__(self,username) -> str:
        self.username = username
    
    @property
    def username(self):
        return self.username

    @username.setter
    def username(self,value):
        if not self.username_length_validator(value):
            raise UsernameLengthError

        if not self.username_starts_alpha(value):
            raise UsernameStartDigitError
        

    def username_length_validator(self, value):
        is_valid = False
        if len(value) > 3:
            is_valid = True

        return is_valid

    def username_starts_alpha(self, value):
        is_valid = False
        if value[0].isalpha():
            is_valid = True

        return is_valid




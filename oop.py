
from validator import(
    UserValidator
)
from helper.exception import(
    UsernameLengthError,
    UsernameStartDigitError
)

class Username:
    @staticmethod
    def check(username):
        is_valid = False
        try:
            username = UserValidator(username)
        except UsernameLengthError as e:
            print(e)
        except UsernameStartDigitError as e:
            print(e)
        else:
            is_valid = True

        return is_valid
        
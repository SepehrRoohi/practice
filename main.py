from getpass import getpass
import oop


class Main():

    def run_shopping_list(self):
        username_valid = False
        password_valid = False
        phone_number = False
        while not username_valid:
            username = input('Enter a Username: ')
            username_valid = oop.Username.check(username)
        password = getpass('Enter a Password: ')
        phone_number = input('Enter a phone number: ')

        print(
            f"\n>> Username: {username}\n>> Password: {password}\n>> Phone number: {phone_number}"
        )


if __name__ == "__main__":
    main = Main()
    main.run_shopping_list()

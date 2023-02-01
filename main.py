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
        

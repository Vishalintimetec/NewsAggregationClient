from client.menus.base import Menu
from client.utils import validate_email, validate_password
import getpass

class SignupMenu(Menu):
    def display(self):
        username = input("Username: ")
        email = input("Email: ")
        if not validate_email(email):
            print("Invalid email format.")
            return
        password = getpass.getpass("Password: ")
        if not validate_password(password):
            print("Password too short.")
            return
        resp = self.user_api.signup(username, email, password)
        if resp.status_code == 201:
            print("Signup successful. Please login.")
        else:
            print("Signup failed:", resp.json().get("detail", resp.text))
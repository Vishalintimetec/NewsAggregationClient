from client.menus.base import Menu
from client.menus.admin import AdminMenu
from client.menus.user import UserMenu
from getpass import getpass

class LoginMenu(Menu):
    def display(self):
        email = input("Email: ")
        password = getpass("Enter your password: ")
        resp = self.user_api.login(email, password)
        if resp.status_code == 200:
            token = resp.json().get("access_token")
            self.user_api.set_token(token)
            self.admin_api.set_token(token)
            self.session.set_token(token)
            user_info = self.user_api.get_user_info().json()
            self.session.set_user_info(user_info)
            print("DEBUG: user_info =", user_info)
            if user_info.get("user_role") == "admin":
                AdminMenu(self.user_api, self.admin_api, self.session).display()
            else:
                UserMenu(self.user_api, self.admin_api, self.session).display()
        else:
            print("Login failed:", resp.json().get("detail", resp.text))
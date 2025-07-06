from client.menus.base import Menu
from client.menus.login import LoginMenu
from client.menus.signup import SignupMenu

class HomeMenu(Menu):
    def display(self):
        while True:
            print("\nWelcome to the News Aggregator application. Please choose:")
            print("1. Login\n2. Sign up\n3. Exit")
            choice = input("Choose: ")
            if choice == "1":
                LoginMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "2":
                SignupMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "3":
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice.")
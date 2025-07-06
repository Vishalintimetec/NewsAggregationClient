from client.menus.base import Menu
from client.menus.headlines import HeadlinesMenu
from client.menus.saved_articles import SavedArticlesMenu
from client.menus.search import SearchMenu
from client.menus.notifications import NotificationsMenu

class UserMenu(Menu):
    def display(self):
        user = self.session.user_info
        while True:
            print(f"\nWelcome to the News Application, {user.get('username', 'User')}!")
            print("1. Headlines\n2. Saved Articles\n3. Search\n4. Notifications\n5. Report Article\n6. Logout")
            choice = input("Choose: ")
            if choice == "1":
                HeadlinesMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "2":
                SavedArticlesMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "3":
                SearchMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "4":
                NotificationsMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "5":
                article_id = input("Enter Article ID to report: ")
                resp = self.user_api.report_article(article_id)
                print(resp.json())
            elif choice == "6":
                break
            else:
                print("Invalid choice.")
from client.menus.base import Menu

class HideUnhideMenu(Menu):
    def display(self):
        print("\nHide/Unhide Menu:")
        print("1. Hide/Unhide Article")
        print("2. Hide/Unhide Category")
        print("3. Back")
        choice = input("Choose: ")
        if choice == "1":
            article_id = input("Enter Article ID: ")
            hide = input("Hide? (y/n): ").lower() == 'y'
            if hide:
                resp = self.admin_api.hide_article(article_id, hide)
            else:
                resp = self.admin_api.unhide_article(article_id, hide)
            print(resp.json())
        elif choice == "2":
            category_id = input("Enter Category ID: ")
            hide = input("Hide? (y/n): ").lower() == 'n'
            resp = self.admin_api.toggle_category(category_id, hide)
            print(resp.json())
        elif choice == "3":
            return
        else:
            print("Invalid choice.")
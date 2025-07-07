from client.menus.base import Menu

class BlockKeywordMenu(Menu):
    def display(self):
        print("\nBlock/Unblock Keyword Menu:")
        print("1. Block Keyword")
        print("2. Unblock Keyword")
        print("3. view all blocked keywords")
        print("4. Back")
        choice = input("Choose: ")
        if choice == "1":
            keyword = input("Enter keyword to block: ")
            resp = self.admin_api.block_keyword(keyword)
            print(resp.json())
        elif choice == "2":
            keyword = input("Enter keyword to unblock: ")
            resp = self.admin_api.unblock_keyword(keyword)
            print(resp.json())
        elif choice == "3":
            resp = self.admin_api.get_blocked_keywords()
            if resp.status_code == 200:
                keywords = resp.json()
                print("\nBlocked Keywords:")
                if keywords:
                    for kw in keywords:
                        print("-", kw)
                else:
                    print("No blocked keywords found.")
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
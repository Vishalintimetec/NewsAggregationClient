from client.menus.base import Menu
from client.menus.hide_unhide import HideUnhideMenu
from client.menus.block_keywords import BlockKeywordMenu
from datetime import datetime

class AdminMenu(Menu):
    def display(self):
        while True:
            print("\nAdmin Menu:")
            print("1. View list of external servers and status")
            print("2. View external server details")
            print("3. Update/Edit external server details")
            print("4. Add new News Category")
            print("5. Hide/Unhide Articles or Categories")
            print("6. Block/Unblock Keywords")
            print("7. Logout")
            choice = input("Choose: ")
            if choice == "1":
                resp = self.admin_api.get_external_servers()
                servers = resp.json()
                print("\nList of external servers:")
                for server_id, server in enumerate(servers, 1):
                    status = "Active" if server.get("is_active") else "Not Active"
                    last_accessed = server.get("last_accessed", "")
                    if last_accessed and "T" in last_accessed:
                        last_accessed = last_accessed.split("T")[0]
                        dt = datetime.strptime(last_accessed, "%Y-%m-%d")
                        last_accessed = dt.strftime("%d %b %Y")
                    print(f"{server_id}. {server.get('server_name', '')} - {status} - last accessed: {last_accessed}")

            elif choice == "2":
                response = self.admin_api.get_external_servers()
                servers = response.json()
                print("\nList of external server details:")
                for idx, server in enumerate(servers, 1):
                    print(f"{idx}. {server.get('server_name', '')} - {server.get('api_key', '<API KEY>')}")
            elif choice == "3":
                server_id = input("Enter server ID: ")
                api_key = input("Enter new API key: ")
                resp = self.admin_api.update_external_server(server_id, api_key)
                print(resp.json())
            elif choice == "4":
                name = input("Enter new category name: ")
                resp = self.admin_api.add_category(name)
                print(resp.json())
            elif choice == "5":
                HideUnhideMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "6":
                BlockKeywordMenu(self.user_api, self.admin_api, self.session).display()
            elif choice == "7":
                break
            else:
                print("Invalid choice.")
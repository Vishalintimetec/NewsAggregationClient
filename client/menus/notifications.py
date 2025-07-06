from client.menus.base import Menu

class NotificationsMenu(Menu):
    def display(self):
        print("\nNotifications Menu:")
        print("1. View Notifications\n2. Configure Notifications\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            notifications = self.user_api.get_notifications()
            notifications = notifications.json()
            if not notifications:
                print("No notifications found.")
                return
            print("\n Notifications:")
            for idx, notif in enumerate(notifications, 1):
                print(f"{idx}. Category: {notif['category'].title()}, Keyword: {notif['keyword']}")

        elif choice == "2":
            self.configure_notifications()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def configure_notifications(self):
        # Get all categories dynamically
        categories_resp = self.user_api.get_all_categories()
        if categories_resp.status_code != 200:
            print("Failed to fetch categories.")
            return
        categories = categories_resp.json()

        print("\nConfigure Notifications:")
        config_data = []

        for cat in categories:
            category_name = cat['category_name']
            enabled = input(f"Enable {category_name}? (y/n): ").lower() == 'y'
            if enabled:
                keywords_input = input(f"Enter keywords for {category_name} (comma separated): ")
                keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
            else:
                keywords = []

            # Use correct keys that match the server schema
            config_data.append({
                "category_name": category_name,
                "category_id": cat['category_id'],
                "is_enabled": enabled,
                "keywords": keywords
            })

        # print("DEBUG: Sending notification config payload:", config_data)
        # Wrap in configurations key
        payload = {"configurations": config_data}
        resp = self.user_api.configure_notifications(payload)

        # Add error handling
        print(f"DEBUG: Response status code: {resp.status_code}")
        print(f"DEBUG: Response text: {resp.text}")

        if resp.status_code == 200:
            try:
                result = resp.json()
                print("Configuration result:", result)
            except Exception as e:
                print(f"Error parsing JSON response: {e}")
        else:
            print(f"Server returned error status: {resp.status_code}")


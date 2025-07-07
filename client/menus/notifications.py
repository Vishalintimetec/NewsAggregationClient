from client.menus.base import Menu

class NotificationsMenu(Menu):

    def display(self):
        print("\nNotifications Menu:")
        print("1. View Notifications\n2. Configure Notifications\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            self.view_notifications()
        elif choice == "2":
            self.configure_notifications()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def view_notifications(self):
        response = self.user_api.get_unread_notifications()
        if not response.ok:
            print("Error fetching notifications.")
            return

        notifications = response.json()
        if not notifications:
            print("No notifications found.")
            return

        print("\nUnread Notifications:")
        for idx, notif in enumerate(notifications, 1):
            print(f"{idx}. Article ID: {notif['article_id']} | Message: {notif['message']}")

    def view_notifications_setting(self):
        notifications = self.user_api.get_notifications_preference()
        notifications = notifications.json()
        if not notifications:
            print("No notifications found.")
            return

        # Group by category
        grouped = {}
        for notif in notifications:
            category = notif['category'].title()
            is_enabled = notif.get('is_enabled', 1)
            keyword = notif.get('keyword')
            if category not in grouped:
                grouped[category] = {
                    "is_enabled": is_enabled,
                    "keywords": []
                }
            # Only add keyword if not None/empty and not already in the list
            if keyword and keyword not in grouped[category]["keywords"]:
                grouped[category]["keywords"].append(keyword)

        print("\nNotifications:")
        for idx, (category, info) in enumerate(grouped.items(), 1):
            keywords = ", ".join(info["keywords"]) if info["keywords"] else "None"
            status = "Enabled" if info["is_enabled"] else "Disabled"
            print(f"{idx}. Category: {category} | Status: {status} | Keywords: {keywords}")

    def configure_notifications(self):
        # Get all categories dynamically
        categories_resp = self.user_api.get_all_categories()
        if categories_resp.status_code != 200:
            print("Failed to fetch categories.")
            return
        categories = categories_resp.json()
        self.view_notifications_setting()
        print("\n\nConfigure Notifications:")
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


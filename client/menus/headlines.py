from client.menus.base import Menu
from client.utils import input_date

class HeadlinesMenu(Menu):
    def display(self):
        print("\nHeadlines Menu:")
        print("1. Today\n2. Date range\n3. Back")
        choice = input("Choose: ")
        if choice == "1":
            self.show_headlines_today()
        elif choice == "2":
            self.show_headlines_date_range()
        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    def show_headlines_today(self):
        # Fetch categories dynamically
        categories = self.get_categories()
        if not categories:
            print("No categories available.")
            return
        print("\nAvailable Categories:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat['category_name']}")
        cat_choice = input("Choose category (number or leave blank for all): ")
        if cat_choice.strip() == "":
            category = None
        else:
            try:
                category = categories[int(cat_choice)-1]['category_name']
            except (IndexError, ValueError):
                print("Invalid choice.")
                return
        resp = self.user_api.get_headlines_today(category=category)
        self.show_article_list_and_select(resp)

    def show_headlines_date_range(self):
        start = input_date("Enter start date (YYYY-MM-DD): ")
        end = input_date("Enter end date (YYYY-MM-DD): ")
        # Fetch categories dynamically
        categories = self.get_categories()
        if not categories:
            print("No categories available.")
            return
        print("\nAvailable Categories:")
        for idx, cat in enumerate(categories, 1):
            print(f"{idx}. {cat['category_name']}")
        cat_choice = input("Choose category (number or leave blank for all): ")
        if cat_choice.strip() == "":
            category = None
        else:
            try:
                category = categories[int(cat_choice)-1]['category_name']
            except (IndexError, ValueError):
                print("Invalid choice.")
                return
        resp = self.user_api.get_headlines_by_date_range(
            start_date=start.isoformat(),
            end_date=end.isoformat(),
            category=category
        )
        self.show_article_list_and_select(resp)

    def get_categories(self):
        resp = self.user_api.get_all_categories()
        if resp.status_code == 200:
            return resp.json()
        else:
            print("Failed to fetch categories.")
            return []

    def show_article_list_and_select(self, resp):
        data = resp.json()
        if isinstance(data, list):
            articles = data
        elif isinstance(data, dict) and "articles" in data:
            articles = data["articles"]
        else:
            articles = []
        if not articles:
            print("No articles found for the selected criteria.")
            return

        # Show only article_id and title
        print("\nAvailable Articles:")
        for art in articles:
            print(f"Article Id: {art.get('article_id', art.get('id'))} | Title: {art.get('title')}")

        # Prompt for article_id to view
        article_id = input("\nEnter Article ID to view full details (or 'b' to go back): ")
        if article_id.lower() == 'b':
            return

        # Find the article
        article = next((a for a in articles if str(a.get('article_id', a.get('id'))) == article_id), None)
        if not article:
            print("Invalid Article ID.")
            return

        # Show full details
        print("\n--- Article Details ---")
        print(f"Article Id: {article.get('article_id', article.get('id'))}")
        print(f"Title: {article.get('title')}")
        print(f"Description: {article.get('description')}")
        print(f"Content: {article.get('content')}")
        print(f"Source: {article.get('source')}")
        print(f"URL: {article.get('url')}")
        print(f"Published At: {article.get('published_at')}")
        print(f"Category: {article.get('category', article.get('category_name', 'N/A'))}")

        # Automatically mark as read
        self.user_api.record_read(article_id)

        # Show actions menu, pass all articles for further actions
        self.headlines_actions(articles)

    def headlines_actions(self, articles):
        while True:
            print("\nHEADLINES ACTIONS")
            print("1. Back")
            print("2. Logout")
            print("3. Save Article")
            print("4. Like Article")
            print("5. Dislike Article")
            action = input("Choose: ")
            if action == "1":
                return
            elif action == "2":
                exit()
            elif action == "3":
                article_id = input("Enter Article ID to save: ")
                save_resp = self.user_api.save_article(article_id)
                print(save_resp.json())
            elif action == "4":
                article_id = input("Enter Article ID to like: ")
                like_resp = self.user_api.like_article(article_id)
                print(like_resp.json())
            elif action == "5":
                article_id = input("Enter Article ID to dislike: ")
                dislike_resp = self.user_api.dislike_article(article_id)
                print(dislike_resp.json())
            else:
                print("Invalid choice.")
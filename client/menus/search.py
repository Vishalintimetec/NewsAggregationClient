from client.menus.base import Menu
from client.utils import input_date

class SearchMenu(Menu):
    def display(self):
        query = input("Enter search query: ")
        start = input_date("Enter start date (YYYY-MM-DD): ")
        end = input_date("Enter end date (YYYY-MM-DD): ")
        resp = self.user_api.search_articles(query, start_date=start.isoformat(), end_date=end.isoformat())
        data = resp.json()
        if resp.status_code == 200:
            # Handle both list and dict with 'articles'
            if isinstance(data, list):
                articles = data
            elif isinstance(data, dict) and "articles" in data:
                articles = data["articles"]
            else:
                articles = []
            if not articles:
                print("No articles found for the search criteria.")
            else:
                for art in articles:
                    print(f"\nArticle Id: {art.get('article_id', art.get('id'))} {art.get('title')}")
                    print(f"{art.get('description')}")
                    print(f"Source: {art.get('source')}")
                    print(f"URL: {art.get('url')}")
                    print(f"Category: {art.get('category', 'N/A')}")
            # Actions menu
            while True:
                print("\nSEARCH RESULTS ACTIONS")
                print("1. Back")
                print("2. Logout")
                print("3. Save Article")
                action = input("Choose: ")
                if action == "1":
                    return  # Go back to previous menu
                elif action == "2":
                    exit()
                elif action == "3":
                    article_id = input("Enter Article ID to save: ")
                    save_resp = self.user_api.save_article(article_id)
                    print(save_resp.json())
                else:
                    print("Invalid choice.")
        else:
            print("Failed to search articles.")
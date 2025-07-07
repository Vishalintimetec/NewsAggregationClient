from client.menus.base import Menu

class SavedArticlesMenu(Menu):
    def display(self):
        resp = self.user_api.get_saved_articles()
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
                print("No saved articles found.")
            else:
                for art in articles:
                    print(f"\nArticle Id: {art.get('article_id', art.get('id'))} {art.get('title')}")
                    print(f"{art.get('description')}")
                    print(f"Source: {art.get('source')}")
                    print(f"URL: {art.get('url')}")
                    print(f"Category: {art.get('category', 'N/A')}")
            # Actions menu
            while True:
                print("\nSAVED ARTICLES ACTIONS")
                print("1. Back")
                print("2. Logout")
                print("3. Delete Article")
                action = input("Choose: ")
                if action == "1":
                    return  # Go back to previous menu
                elif action == "2":
                    exit()
                elif action == "3":
                    article_id = input("Enter Article ID to delete: ")
                    del_resp = self.user_api.delete_saved_article(article_id)
                    print(del_resp.json())
                else:
                    print("Invalid choice.")
        else:
            print("Failed to fetch saved articles.")
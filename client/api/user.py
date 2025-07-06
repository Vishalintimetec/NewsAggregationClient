import requests
from client.api.base import BaseAPIClient
from client.config import SERVER_URL

class UserAPIClient(BaseAPIClient):
    def login(self, email, password):
        return requests.post(f"{SERVER_URL}/auth/login", json={"email": email, "password": password})

    def signup(self, username, email, password):
        return requests.post(f"{SERVER_URL}/auth/signup", json={"username": username, "email": email, "password": password})

    def get_user_info(self):
        return requests.get(f"{SERVER_URL}/user/me", headers=self._headers())

    def get_headlines_today(self, category=None):
        params = {}
        if category:
            params["category"] = category
        return requests.get(f"{SERVER_URL}/user/headlines/today", headers=self._headers(), params=params)

    def get_headlines_by_date_range(self, start_date, end_date, category=None):
        params = {"start_date": start_date, "end_date": end_date}
        if category:
            params["category"] = category
        return requests.get(f"{SERVER_URL}/user/headlines/date-range", headers=self._headers(), params=params)

    def save_article(self, article_id):
        return requests.post(f"{SERVER_URL}/user/save_article/{article_id}", headers=self._headers())

    def get_saved_articles(self):
        return requests.get(f"{SERVER_URL}/user/saved_articles", headers=self._headers())

    def delete_saved_article(self, article_id):
        return requests.delete(f"{SERVER_URL}/user/delete_article/{article_id}", headers=self._headers())

    def search_articles(self, query, start_date=None, end_date=None, sort_by="likes"):
        params = {"query": query, "sort_by": sort_by}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return requests.get(f"{SERVER_URL}/user/search", headers=self._headers(), params=params)

    def report_article(self, article_id):
        return requests.post(f"{SERVER_URL}/report_article/report", headers=self._headers(), json={"article_id": article_id})

    def get_notifications(self):
        return requests.get(f"{SERVER_URL}/notifications/preferences", headers=self._headers())

    def configure_notifications(self, config_data):
        return requests.post(f"{SERVER_URL}/notifications/configure-notifications", headers=self._headers(), json=config_data)

    def record_read(self, article_id):
        return requests.post(f"{SERVER_URL}/read-history/read/{article_id}", headers=self._headers())

    def like_article(self, article_id):
        return requests.post(f"{SERVER_URL}/preferences/like/{article_id}", headers=self._headers())

    def dislike_article(self, article_id):
        return requests.post(f"{SERVER_URL}/preferences/dislike/{article_id}", headers=self._headers())

    def get_all_categories(self):
        return requests.get(f"{SERVER_URL}/categories/all", headers=self._headers())
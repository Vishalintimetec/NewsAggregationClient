import requests
from client.api.base import BaseAPIClient
from client.config import SERVER_URL

class UserAPIClient(BaseAPIClient):

    def login(self, email, password):
        try:
            return requests.post(f"{SERVER_URL}/auth/login", json={"email": email, "password": password})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def signup(self, username, email, password):
        try:
            return requests.post(f"{SERVER_URL}/auth/signup", json={"username": username, "email": email, "password": password})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_user_info(self):
        try:
            return requests.get(f"{SERVER_URL}/user/me", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_headlines_today(self, category=None):
        try:
            params = {}
            if category:
                params["category"] = category
            return requests.get(f"{SERVER_URL}/user/headlines/today", headers=self._headers(), params=params)
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_headlines_by_date_range(self, start_date, end_date, category=None):
        try:
            params = {"start_date": start_date, "end_date": end_date}
            if category:
                params["category"] = category
            return requests.get(f"{SERVER_URL}/user/headlines/date-range", headers=self._headers(), params=params)
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def save_article(self, article_id):
        try:
            return requests.post(f"{SERVER_URL}/user/save_article/{article_id}", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_saved_articles(self):
        try:
            return requests.get(f"{SERVER_URL}/user/saved_articles", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def delete_saved_article(self, article_id):
        try:
            return requests.delete(f"{SERVER_URL}/user/delete_article/{article_id}", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def search_articles(self, query, start_date=None, end_date=None):
        data = {"keyword": query}
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        try:
            return requests.post(f"{SERVER_URL}/user/search", json=data, headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def report_article(self, article_id):
        try:
            return requests.post(f"{SERVER_URL}/report_article/report", headers=self._headers(), json={"article_id": article_id})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_notifications_preference(self):
        try:
            return requests.get(f"{SERVER_URL}/notifications/preferences", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def configure_notifications(self, config_data):
        try:
            return requests.post(f"{SERVER_URL}/notifications/configure-notifications", headers=self._headers(), json=config_data)
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_unread_notifications(self):
        try:
            return requests.get(f"{SERVER_URL}/notifications/unread", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def record_read(self, article_id):
        try:
            return requests.post(f"{SERVER_URL}/read-history/read/{article_id}", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def like_article(self, article_id):
        try:
            return requests.post(f"{SERVER_URL}/preferences/like/{article_id}", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def dislike_article(self, article_id):
        try:
            return requests.post(f"{SERVER_URL}/preferences/dislike/{article_id}", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_all_categories(self):
        try:
            return requests.get(f"{SERVER_URL}/categories/all", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}
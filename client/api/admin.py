import requests
from client.api.base import BaseAPIClient
from client.config import SERVER_URL

class AdminAPIClient(BaseAPIClient):
    def get_external_servers(self):
        try:
            return requests.get(f"{SERVER_URL}/external-servers/all", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def update_external_server(self, server_id, api_key):
        try:
            return requests.put(f"{SERVER_URL}/external-servers/{server_id}", headers=self._headers(),
                                json={"api_key": api_key})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def add_category(self, name):
        try:
            return requests.post(f"{SERVER_URL}/categories", headers=self._headers(), json={"name": name})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def hide_article(self, article_id, hide=True):
        try:
            return requests.put(f"{SERVER_URL}/report_article/admin/articles/{article_id}/hide",
                                headers=self._headers(), json={"hide": hide})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def unhide_article(self, article_id, hide=False):
        try:
            return requests.put(f"{SERVER_URL}/report_article/admin/articles/{article_id}/unhide",
                                headers=self._headers(), json={"hide": hide})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def toggle_category(self, category_id, is_visible: bool):
        try:
            return requests.put(f"{SERVER_URL}/categories/admin/category/{category_id}/visibility",
                                headers=self._headers(), json={"is_visible": is_visible})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def block_keyword(self, keyword):
        try:
            return requests.post(f"{SERVER_URL}/admin/keywords/block", headers=self._headers(),
                                 json={"keyword": keyword})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def unblock_keyword(self, keyword):
        try:
            return requests.post(f"{SERVER_URL}/admin/keywords/unblock", headers=self._headers(),
                                 json={"keyword": keyword})
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

    def get_blocked_keywords(self):
        try:
            return requests.get(f"{SERVER_URL}/admin/keywords/", headers=self._headers())
        except requests.exceptions.ConnectionError:
            return {"error": "Server is not reachable."}

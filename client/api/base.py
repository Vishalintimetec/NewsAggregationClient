from client.config import SERVER_URL

class BaseAPIClient:
    def __init__(self):
        self.token = None

    def set_token(self, token):
        self.token = token

    def _headers(self):
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}
        return {}
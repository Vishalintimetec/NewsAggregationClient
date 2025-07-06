class Session:
    def __init__(self):
        self.token = None
        self.user_info = None

    def set_token(self, token):
        self.token = token

    def set_user_info(self, user_info):
        self.user_info = user_info

    def clear(self):
        self.token = None
        self.user_info = None
class Menu:
    def __init__(self, user_api, admin_api, session):
        self.user_api = user_api
        self.admin_api = admin_api
        self.session = session

    def display(self):
        raise NotImplementedError
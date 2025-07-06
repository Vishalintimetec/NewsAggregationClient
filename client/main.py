from client.api.user import UserAPIClient
from client.api.admin import AdminAPIClient
from client.session import Session
from client.menus.home import HomeMenu

if __name__ == "__main__":
    user_api = UserAPIClient()
    admin_api = AdminAPIClient()
    session = Session()
    HomeMenu(user_api, admin_api, session).display()

    
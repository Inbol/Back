from app.services import user_service

def get_all_users():
    return user_service.list_users()

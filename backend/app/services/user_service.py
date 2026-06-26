from backend.app.crud.user import create_user as db_create_user


def register_user(user_data):
    # здесь будет бизнес-логика
    # например: проверка email, password rules
    return db_create_user(user_data)
def create_user(user_data):
    # пока просто заглушка
    return {
        "id": 1,
        "email": user_data.get("email"),
        "username": user_data.get("username")
    }
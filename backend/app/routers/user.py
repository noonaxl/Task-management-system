from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users():
    return {"message": "get users list"}


@router.post("/")
def create_user():
    return {"message": "user created"}
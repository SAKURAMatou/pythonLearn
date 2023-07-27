from fastapi import APIRouter

# APIRouter的实例对象等效于FastAPI的实例对象
router = APIRouter()


@router.get("/users")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}

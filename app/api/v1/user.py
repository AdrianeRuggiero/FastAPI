from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
async def read_items():
    return[{"username": " Yasmina"}]

@router.get("/user_all")
async def read_items():
    return[{"user_name": "Adriane"}, {"user_name": "Vanessa"}]
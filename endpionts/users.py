from fastapi import APIRouter, Depends
from repositories.users import UserRep
from .depends import get_user_repository
from typing import List
from models.user import User, UserIn

router = APIRouter()


@router.get("/", response_model=List[User])
async def read_users(
    users: UserRep = Depends(get_user_repository),
    limit: int = 100,
    skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/', response_model=User)
async def create(
    user: UserIn,
    users: UserRep = Depends(get_user_repository)):
    return await users.create(instance=user)

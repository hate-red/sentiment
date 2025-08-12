from fastapi import APIRouter, Depends, HTTPException, status
from app.users.service import UserService
from app.users.schemas import UserRB, UserPublic


router = APIRouter(prefix='/u', tags=['works with users'])


@router.get('/profiles', summary='Gets users')
async def get_profile(user: UserRB = Depends()):
    users = await UserService.get_all(**user.to_dict())

    return users


@router.get('/profile', summary='Gets user profile')
async def get_profile(user_id: int):
    user = await UserService.get_user(user_id)

    return user
  

from fastapi import APIRouter, Depends, HTTPException, status
from app.users.service import UserService
from app.users.schemas import UserRB, UserPublic


router = APIRouter(prefix='/u', tags=['works with users'])


@router.get('/profiles', summary='get user profiles')
async def get_profile(user: UserRB = Depends()) -> list[UserPublic] | dict:
    users = await UserService.get(**user.to_dict())

    if users:
        return users
    
    return {'detail': 'No users were found'}


@router.get('/profile', summary='get user profile')
async def get_profile(user_id: int) -> UserPublic | dict:
    user = await UserService.get_one_or_none_by_id(id=user_id)

    if user:
        return user

    return {'detail': 'Profile not found'}

from fastapi import APIRouter, Depends, HTTPException, status
from app.users.service import UserService
from app.users.schemas import UserRB, UserPublic, UserAdd


router = APIRouter(prefix='/u', tags=['Users'])


@router.get('/profiles', summary='Gets users')
async def get_profiles(filter_by: UserRB = Depends()) -> list[UserPublic] | dict:
    users = await UserService.get_users(**filter_by.to_dict())

    return users


@router.get('/profile', summary='Gets user profile')
async def get_profile(user_id: int) -> UserPublic:
    user = await UserService.get_user(user_id)

    return user


@router.post('/create')
async def create_user(user: UserAdd = Depends()) -> dict:
    check = await UserService.add(**user.dict())

    if check:
        return {
            'message': 'User was sucessfully created',
            'user': user
        }

    return {'detail': 'Error when creating user'}

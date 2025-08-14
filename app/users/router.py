from fastapi import APIRouter, Depends

from app.users.service import UserService
from app.users.schemas import UserFilter, UserPublic, UserCreate, UserUpdate, UserDelete

router = APIRouter(prefix='/u', tags=['Users'])


@router.get('/profiles', summary='Gets users')
async def get_profiles(filter_by: UserFilter = Depends()) -> list[UserPublic] | dict:
    users = await UserService.get_users(**filter_by.to_dict())

    return users


@router.get('/profile', summary='Gets user profile')
async def get_profile(user_id: int) -> UserPublic:
    user = await UserService.get_user(user_id)

    return user


@router.post('/create', summary='Creates new user')
async def create_user(user: UserCreate = Depends()) -> dict:
    check = await UserService.create(**user.model_dump())

    if check:
        return {
            'message': 'User was successfully created',
            'user': user
        }

    return {'detail': 'Error when creating user'}


@router.put('/update', summary='Changes user information')
async def update_user(user_id: int, user_info: UserUpdate = Depends()) -> UserPublic | dict:
    check = await UserService.update(filter_by={'id': user_id}, **user_info.model_dump())

    if check:
        user = await UserService.get_user(user_id)
        return user

    return {'detail': 'Error when updating user information'}


@router.delete('/delete', summary='Deletes user')
async def delete_user(user: UserDelete = Depends()) -> dict:
    check = await UserService.delete(**user.to_dict())

    if check:
        return {'message': 'User was successfully deleted'}

    return {'detail': 'Error when deleting user'}

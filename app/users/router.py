from http.client import responses

from fastapi import APIRouter, Depends, HTTPException, status, Response

from app.users.dependencies import get_current_user, get_current_admin
from app.users.service import UserService
from app.users.schemas import UserFilter, UserPublic, UserSignUp, UserSignIn, UserUpdate, UserDelete
from app.users.models import User
from app.users.auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(prefix='/u', tags=['Users'])


@router.post('/signup', summary='Registers user')
async def signup(user_info: UserSignUp = Depends()) -> dict:
    check_email = await UserService.get_one_or_none(email=user_info.email)
    if check_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with this email already exists'
        )

    check_username = await UserService.get_one_or_none(username=user_info.username)
    if check_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with this username already exists'
        )

    user_dict = user_info.model_dump()
    user_dict['password'] = get_password_hash(str(user_info.password))
    await UserService.create(**user_dict)

    return {'message': 'User was sucessfully signed up'}


@router.post('/signin', summary='Logs user in')
async def signin(response: Response, user_info: UserSignIn = Depends()) -> dict:
    user = await authenticate_user(email=user_info.email, password=str(user_info.password))

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid email or password')

    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie(key='user_access_token', value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.post('/logout', summary='Logs user out')
async def logout(response: Response) -> dict:
    response.delete_cookie(key='user_access_token')
    return {'message': 'User was logged out'}


@router.get('/profile', summary='Gets user profile')
async def get_profile(user: UserPublic = Depends(get_current_user)) -> UserPublic:
    return user


@router.put('/update', summary='Changes user information')
async def update_user(user_id: int, user_info: UserUpdate = Depends()) -> UserPublic | dict:
    check = await UserService.update(filter_by={'id': user_id}, **user_info.model_dump())

    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error when updating user information')

    user = await UserService.get_user(user_id)
    return user


@router.delete('/delete', summary='Deletes user')
async def delete_user(user: UserDelete = Depends()) -> dict:
    check = await UserService.delete(**user.to_dict())

    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Error when deleting user')

    return {'message': 'User was successfully deleted'}


@router.get('/find', summary='Finds users')
async def find_users(filter_by: UserFilter = Depends()) -> list[UserPublic] | dict:
    users = await UserService.get_users(**filter_by.to_dict())

    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found')

    return users


@router.get('/all', summary='Finds all users (for admins or higher)')
async def find_all_users(user: UserPublic = Depends(get_current_admin)) -> list[UserPublic]:
    users = await UserService.get_users()
    return users
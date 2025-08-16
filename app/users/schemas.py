from pydantic import BaseModel, ConfigDict, Field, EmailStr, SecretStr
from app.history.schemas import HistoryPublic

class UserPublic(BaseModel):
    """Describes response model"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    history: list['HistoryPublic']

    is_user: bool
    is_premium: bool
    is_admin: bool
    is_super_admin: bool


class UserFilter(BaseModel):
    """Use to get filtered list of users"""

    model_config = ConfigDict(from_attributes=True)

    username: str | None = None
    email: EmailStr | None = None

    is_user: bool | None = True
    is_premium: bool | None = False
    is_admin: bool | None = False
    is_super_admin: bool | None = False


    def to_dict(self):
        data = {
            'username': self.username, 
            'email': self.email, 
            'is_user': self.is_user,
            'is_premium': self.is_premium,
            'is_admin': self.is_admin,
            'is_super_admin': self.is_super_admin
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data


class UserSignUp(BaseModel):
    """Use to create new user"""

    username: str
    email: EmailStr
    password: SecretStr

    is_user: bool | None = True
    is_premium: bool | None = False
    is_admin: bool | None = False
    is_super_admin: bool | None = False


class UserSignIn(BaseModel):
    email: EmailStr
    password: SecretStr = Field(..., min_length=8, max_length=50)


class UserUpdate(BaseModel):
    """Use both for updating user information"""

    username: str
    email: EmailStr

    is_user: bool | None = True
    is_premium: bool | None = False
    is_admin: bool | None = False
    is_super_admin: bool | None = False


class UserDelete(BaseModel):
    """Use to delete users"""

    id: int | None = None
    username: str | None = None
    email: EmailStr | None = None

    is_user: bool | None = True
    is_premium: bool | None = False
    is_admin: bool | None = False
    is_super_admin: bool | None = False


    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_user': self.is_user,
            'is_premium': self.is_premium,
            'is_admin': self.is_admin,
            'is_super_admin': self.is_super_admin
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data
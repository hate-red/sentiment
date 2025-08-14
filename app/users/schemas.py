from pydantic import BaseModel, ConfigDict, Field, EmailStr
from app.history.schemas import HistoryPublic

class UserPublic(BaseModel):
    """Describes response model"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    role: str
    history: list["HistoryPublic"]


class UserFilter(BaseModel):
    """Use to get filtered list of users"""

    model_config = ConfigDict(from_attributes=True)

    username: str | None = None
    email: EmailStr | None = None
    role: str | None = 'default'


    def to_dict(self):
        data = {
            'username': self.username, 
            'email': self.email, 
            'role': self.role, 
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data



class UserCreate(BaseModel):
    """Use to create new user"""

    username: str
    email: EmailStr
    role: str | None = 'default'


class UserUpdate(BaseModel):
    """Use both for updating user information"""

    username: str
    email: EmailStr
    role: str | None = 'default'


class UserDelete(BaseModel):
    """Use to delete users"""

    id: int | None = None
    username: str | None = None
    email: EmailStr | None = None
    role: str | None = 'default'


    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data
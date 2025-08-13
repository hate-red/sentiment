from pydantic import BaseModel, ConfigDict, Field, EmailStr
from app.history.schemas import HistoryPublic

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., gt=0)
    username: str = Field(..., min_length=4, max_length=20)
    email: EmailStr
    role: str = Field(..., description="Characterizes one's privileges")
    history: list["HistoryPublic"] = Field(default=None, description='history')


class UserRB(BaseModel):
    id: int | None = None
    username: str | None = None
    email: EmailStr | None = None
    role: str | None = None


    def to_dict(self):
        data = {
            'id': self.id, 
            'username': self.username, 
            'email': self.email, 
            'role': self.role, 
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data


class UserAdd(BaseModel):
    username: str
    email: EmailStr
    role: str | None = 'default'

from pydantic import BaseModel, ConfigDict, Field, EmailStr, validator


class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., gt=0, description="ID")
    username: str = Field(..., min_length=4, max_length=20, description='Nickname')
    email: EmailStr = Field(..., description='Email')
    role: str = Field(..., description="Characterizes one's privileges")


class UserRB(BaseModel):
    id: int | None = None
    username: str | None = None
    email: EmailStr | None = None
    role: str | None = None


    def to_dict(self):
        data = {'id': self.id, 'username': self.username, 'email': self.email, 'role': self.role}
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data

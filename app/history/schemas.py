from pydantic import BaseModel, ConfigDict, Field, EmailStr


class HistoryPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    avg_sentiment: float


class HistoryRB(BaseModel):
    id: int | None = None
    content: str | None = None
    avg_sentiment: float | None = None
    user_id: int | None = None


    def to_dict(self):
        data = {
            'id': self.id, 
            'content': self.content,
            'avg_sentiment': self.avg_sentiment,
            'user_id': self.user_id
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data

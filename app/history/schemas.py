from pydantic import BaseModel, ConfigDict


class HistoryPublic(BaseModel):
    """Describes response model"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    content: str
    avg_sentiment: float
    user_id: int


class HistoryFilter(BaseModel):
    """Use to get filtered history list"""

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

class HistoryAdd(BaseModel):
    """Use to add new history to a given user"""

    user_id: int
    content: str
    avg_sentiment: float


class HistoryUpdate(BaseModel):
    """Use to update users' history"""

    content: str
    avg_sentiment: float


class HistoryDelete(BaseModel):
    """Use to delete history"""

    id: int | None = None
    user_id: int | None = None
    content: str | None = None
    avg_sentiment: float | None = None


    def to_dict(self):
        data = {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'avg_sentiment': self.avg_sentiment
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}

        return filtered_data
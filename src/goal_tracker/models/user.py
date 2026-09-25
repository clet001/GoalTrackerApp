import uuid
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    id: UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime
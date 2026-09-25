import uuid
from dataclasses import Field
from datetime import datetime
from uuid import UUID

import datetime
from pydantic import BaseModel


class user(BaseModel):
    username: str
    email: str
    id: UUID = Field(default_factory=uuid)
    created_at: datetime
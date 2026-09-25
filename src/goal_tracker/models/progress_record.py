from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ProgressRecord(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    goal_id: UUID
    progress: int
    note: str
    recorded_at: datetime
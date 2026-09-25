from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProgressRecord(BaseModel):
    id: UUID
    goal_id: UUID
    progress: float
    note: str
    recorded_at: datetime
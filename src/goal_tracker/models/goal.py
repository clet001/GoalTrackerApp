from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime, timezone
from pydantic import BaseModel, Field
from pydantic_extra_types.epoch import Integer

class GoalStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    AT_RISK = "at_risk"
    COMPLETED = "completed"
    PAUSED = "paused"

class Goal(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    user_id: Optional[UUID] = Field(default_factory=uuid4)
    title: str
    description: str
    start_date: date
    target_date: date
    status: GoalStatus
    progress: Integer
    created_at: datetime
    updated_at: datetime
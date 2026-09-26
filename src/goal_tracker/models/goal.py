from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime, timezone
from pydantic import BaseModel, Field


class GoalStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    AT_RISK = "at_risk"
    COMPLETED = "completed"
    PAUSED = "paused"

class Goal(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    title: str
    description: str
    start_date: date
    target_date: date
    status: GoalStatus = GoalStatus.NOT_STARTED
    progress: int = Field(ge=0, le=100)
    completed_at: Optional[datetime] = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
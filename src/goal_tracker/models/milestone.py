import uuid
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class MilestoneStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"



class Milestone(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    goal_id:UUID
    title: str
    description: str
    target_date: datetime
    status: MilestoneStatus
    completed_at: Optional[datetime]= None
    
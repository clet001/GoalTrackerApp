import uuid
from datetime import datetime
from enum import Enum
from uuid import UUID

import Field
from pydantic import BaseModel


class MilestoneStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"



class milestone(BaseModel):
    id: UUID = Field(default_factory=uuid)
    goal_id:UUID
    title: str
    description: str
    target_date: datetime
    status: MilestoneStatus
    completed_at: datetime
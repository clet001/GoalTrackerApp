import uuid
from enum import Enum
from uuid import UUID

from datetime import datetime
from pydantic import BaseModel, Field


class CheckinStatus(str, Enum):
    SCHEDULED = "scheduled"
    SENT = "sent"
    RESPONDED = "responded"
    MISSED = "missed"


class Checkin(BaseModel):
    id:UUID = Field(default_factory=uuid.uuid4)
    goal_id: UUID
    scheduled_for: datetime
    status: CheckinStatus = CheckinStatus.SCHEDULED
    response:str | None = None
    responded_at: datetime | None = None
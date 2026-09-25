from enum import Enum
from uuid import UUID

from DateTime import DateTime
from pydantic import BaseModel

class CheckinStatus(str, Enum):
    SCHEDULED = "scheduled"
    SENT = "sent"
    RESPONDED = "responded"
    MISSED = "missed"


class Checkin(BaseModel):
    id:UUID
    goal_id: UUID
    scheduled_for: DateTime
    status: CheckinStatus
    response:str
    responded_at: DateTime
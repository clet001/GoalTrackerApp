from abc import ABC
from uuid import UUID

import CheckIn

from goal_tracker.models.checkin import Checkin


class CheckinRepository(ABC):
    def create_checkin(self, checkin: Checkin) -> Checkin:
        ...
    def get_checkin_by_id(self, checkin_id: UUID) -> Checkin:
        ...
    def update_checkin(self, checkin: Checkin) -> Checkin:
        ...
    def get_pending_checkins(self) -> list[Checkin]:
        ...
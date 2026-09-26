from abc import abstractmethod, ABC
from uuid import UUID

from goal_tracker.models.progress_record import ProgressRecord


class ProgressRecordRepository(ABC):
    @abstractmethod
    def create_progress_record(self, progress_record: ProgressRecord) -> ProgressRecord:
        ...
    @abstractmethod
    def get_progress_by_goal_id(self, progress_record_goal:UUID) -> list[ProgressRecord]:
        ...
    @abstractmethod
    def get_progress(self, progress_id:UUID) -> ProgressRecord:
        ...


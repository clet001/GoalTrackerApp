from abc import ABC, abstractmethod
from uuid import UUID

from goal_tracker.models.milestone import Milestone


class MilestoneRepository(ABC):
    @abstractmethod
    def create_milestone(self, milestone: Milestone) -> Milestone:
        ...
    def get_milestone(self, milestone_id: int) -> Milestone:
        ...
    def update_milestone(self, milestone: Milestone) -> Milestone:
        ...
    def delete_milestone(self, milestone_id: UUID) -> Milestone:
        ...
    def get_milestones_by_goal(self, goal_id: UUID) -> list[Milestone]:
        ...
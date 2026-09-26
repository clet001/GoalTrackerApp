from abc import ABC, abstractmethod
from uuid import UUID

from goal_tracker.models.goal import Goal


class GoalRepository(ABC):
    @abstractmethod
    def create_goal(self, goal:Goal) -> Goal:
        ...
    @abstractmethod
    def update_goal(self, goal_id: UUID, goal: Goal) -> Goal:
        ...
    @abstractmethod
    def delete_goal(self, goal_id: UUID) -> None:
        ...
    @abstractmethod
    def get_goal_by_id(self, goal_id: UUID) -> Goal:
        ...
    @abstractmethod
    def get_goal_by_title(self, goal_title:str) -> list[Goal]:
        ...
from uuid import UUID

from goal_tracker.models.goal import Goal
from goal_tracker.repositories.goal_repository import GoalRepository


class GoalService:

    def __init__(self, repository: GoalRepository):
        self.repository = repository

    def create_goal(self, goal: Goal) -> Goal:
            return self.repository.create_goal(goal)

    def create_goal(self, goal: Goal) -> Goal:
        return self.repository.create_goal(goal)

    def get_goal_by_id(self, goal_id: UUID) -> Goal:
        goal = self.repository.get_goal_by_id(goal_id)

        if goal is None:
            raise ValueError("Goal not found")

        return goal

    def update_goal(self, goal_id: UUID, goal: Goal) -> Goal:
        return self.repository.update_goal(goal_id, goal)

    def delete_goal(self, goal_id: UUID) -> None:
        existing_goal = self.repository.get_goal_by_id(goal_id)

        if existing_goal is None:
            raise ValueError("Goal not found")

        self.repository.delete_goal(goal_id)

    def update_goal(self, goal_id: UUID, goal: Goal) -> Goal:
        existing_goal = self.repository.get_goal_by_id(goal_id)

        if existing_goal is None:
            raise ValueError("Goal not found")

        return self.repository.update_goal(goal_id, goal)


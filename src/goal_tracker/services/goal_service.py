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
        return self.repository.get_goal_by_id(goal_id)
from unittest.mock import Mock
from uuid import uuid4
from datetime import date

import UUID

from goal_tracker.models.goal import Goal
from goal_tracker.repositories.goal_repository import GoalRepository
from goal_tracker.services.goal_service import GoalService


def test_that_goal_can_be_created():
    repository = Mock(spec=GoalRepository)
    service = GoalService(repository)

    goal = Goal(
        user_id=uuid4(),
        title="Software Engineering",
        description="Learn Frontend",
        start_date=date.today(),
        target_date=date(2026, 12, 31),
        progress=0
    )

    service.create_goal(goal)

    repository.create_goal.assert_called_once_with(goal)

def test_that_created_goal_is_returned():
    repository = Mock(spec=GoalRepository)

    goal = Goal(
        user_id=uuid4(),
        title="Learn Python",
        description="Learn Python programming",
        start_date=date.today(),
        target_date=date(2026, 12, 31),
        progress=0
    )

    repository.create_goal.return_value = goal

    service = GoalService(repository)

    result = service.create_goal(goal)

    assert result == goal


def test_that_goal_can_be_found_by_id():
    repository = Mock(spec=GoalRepository)
    service = GoalService(repository)

    goal_id = uuid4()

    service.get_goal_by_id(goal_id)

    repository.get_goal_by_id.assert_called_once_with(goal_id)
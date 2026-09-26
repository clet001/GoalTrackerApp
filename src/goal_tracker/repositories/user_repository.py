from abc import ABC, abstractmethod
from uuid import UUID

from goal_tracker.models.user import User


class UserRepository(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        ...

    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> User:
        ...

    @abstractmethod
    def update(self, user: User) -> User:
        ...

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        ...
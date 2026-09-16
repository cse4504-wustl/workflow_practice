from typing import List, Optional

from entity.task import Task


class InMemoryTaskRepository:
    def __init__(self):
        self._tasks: List[Task] = []

    def get_all(self) -> List[Task]:
        return self._tasks

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return None

    def add(self, task: Task) -> None:
        pass

    def update(self, task: Task) -> None:
        pass

    def remove(self, task_id: int) -> None:
        pass

    def next_id(self) -> int:
        return max([task.id for task in self._tasks], default=0) + 1

from dto.complete_task_request import CompleteTaskRequest
from dto.task_operation_response import TaskOperationResponse
from interfaces.task_repository import TaskRepository


class CompleteTaskUseCase:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def __call__(self, request: CompleteTaskRequest) -> TaskOperationResponse:
        """Retrieve the task via repo.get_by_id(), set completed=True, persist via repo.update().
        Return TaskOperationResponse with success=True if found, success=False otherwise."""
        return None

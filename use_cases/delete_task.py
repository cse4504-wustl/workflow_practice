from dto.task_operation_request import TaskOperationRequest
from dto.task_operation_response import TaskOperationResponse
from interfaces.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def __call__(self, request: TaskOperationRequest) -> TaskOperationResponse:
        """Confirm the task exists via repo.get_by_id(), remove it via repo.remove().
        Return TaskOperationResponse with success=True and the task description if found, or success=False and description="no task found" otherwise."""
        return None

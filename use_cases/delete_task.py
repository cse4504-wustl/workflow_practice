from dto.delete_task_request import DeleteTaskRequest
from dto.task_operation_response import TaskOperationResponse
from interfaces.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def __call__(self, request: DeleteTaskRequest) -> TaskOperationResponse:
        """Confirm the task exists via repo.get_by_id(), remove it via repo.remove().
        Return TaskOperationResponse with success=True if found, success=False otherwise."""
        return None

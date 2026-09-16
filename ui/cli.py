from dto.add_task_request import AddTaskRequest
from dto.complete_task_request import CompleteTaskRequest
from dto.delete_task_request import DeleteTaskRequest
from persistence.in_memory_task_repository import InMemoryTaskRepository
from use_cases.add_task import AddTaskUseCase
from use_cases.complete_task import CompleteTaskUseCase
from use_cases.delete_task import DeleteTaskUseCase
from use_cases.list_tasks import ListTasksUseCase


class TaskCLI:
    def __init__(self):
        repo = InMemoryTaskRepository()
        self.add_task = AddTaskUseCase(repo)
        self.complete_task = CompleteTaskUseCase(repo)
        self.delete_task = DeleteTaskUseCase(repo)
        self.list_tasks = ListTasksUseCase(repo)

    def run(self):
        # Display a menu with options:
        #   1. Add task
        #   2. List tasks
        #   3. Complete task
        #   4. Delete task
        #   5. Quit
        #
        # Handle user input and invoke the appropriate use case as a callable.
        # Save tasks after each modification.
        # Continue looping until user chooses to quit.
        #
        # Example interaction:
        #   === Task Manager ===
        #   1. Add task
        #   2. List tasks
        #   3. Complete task
        #   4. Delete task
        #   5. Quit
        #   Choice: 1
        #   Enter task description: Do homework
        #   Task added successfully!
        #
        # For list tasks, show format like:
        #   ID: 1 | Description: Do homework | Status: Pending | Created: 2024-01-15
        pass


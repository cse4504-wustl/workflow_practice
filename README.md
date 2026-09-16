# Workflow Practice Studio
## Overview
The purpose of this studio is to practice the workflow we will be using in class. Please follow the instructions closely.

In this exercise, you will build a basic command-line task manager where users can add, list, mark as complete, and delete tasks. Below is an example of how this tool would be used:

```
python cli.py add "Buy groceries"
python cli.py add "Do cse4504 homework"
python cli.py list
python cli.py complete 1
python cli.py delete 2
python cli.py save 'my_tasks.csv'
```

In this exercise, you will work through the typical steps that you will need to design and implement a specific feature of your semester project.

Typically, your team will be responsible for the design, implementation, and testing of your software features. However, to speed up the process for this studio, the design will be provided for you.

The main components of this tool are:
1. Task - main datastructure used by this tool
1. Request models - one file per use case, each wrapping the input data for a use case
1. Response models - one file per distinct return shape, wrapping the output data for a use case
1. TaskRepository - Protocol defining the data access interface used by the use cases
1. InMemoryTaskStorage - in-memory implementation of TaskRepository
1. Use cases - one file per operation, each implementing a single task operation
1. TaskStorage - saves/retrieves tasks to/from permanent storage
1. TaskCLI - command line interface (CLI), reading and responding to user input

The components interact with each other as follows:
1. TaskCLI will initialize the use case and TaskStorage objects
1. TaskCLI will interact with the user, parse the user input, and call on the appropriate use case or TaskStorage to complete the request.
1. Each use case class will perform its single operation
1. TaskStorage will read from/write to a file.

## Detailed Instructions

### Step 0
Everyone, clone the team repository to your computer.

### Step 1
Complete this step together, as a team.

1. One person from the team, create a feature branch from the main branch. Give your branch some reasonable name, for example: feature_1. To do this, from the main branch of your repository clone run:
```
git branch feature_1
git checkout feature_1
git push --set-upstream origin feature_1
```
Of course, if you name your branch something other than feature_1, you would use your branch name in these commands.

### Step 2
Everyone:
- Run `git pull` on your clone of the repository, to get the new branch.
- Run `git checkout feature_1` to switch to your new branch.

### Step 3
Complete this step together, as a team.
Typically, you would design the interfaces/contracts for the main components of your feature, and convert this design into code, leaving out the details of the implementation. The interfaces/contracts of your components are the details that other developers need to know when using your components:
- How do I instantiate this component?
- What data/variables can I access from this component?
- What functions can I call on this component?
- What arguments do I need to pass to these functions?
- What data do the functions return?

Interfaces/contracts are just a high level sketch of the components, without the detailed implementation. Of course, in order for the code to work, some kind of implementation is needed. To support this, just have your functions return some dummy value that's consistent with that function's return data type.

The skeleton files are already in the repository. These skeleton files are an example of what your team would produce during the design step. Review these files now.

- `entity/task.py` — `Task` data class
- `dto/add_task_request.py`, `dto/task_operation_request.py` — request models
- `dto/add_task_response.py`, `dto/task_operation_response.py`, `dto/list_tasks_response.py` — response models
- `interfaces/task_repository.py` — `TaskRepository` Protocol
- `persistence/in_memory_task_repository.py` — `InMemoryTaskRepository`
- `use_cases/add_task.py`, `use_cases/complete_task.py`, `use_cases/delete_task.py`, `use_cases/list_tasks.py` — use cases
- `ui/cli.py` — `TaskCLI`
- `main.py` — entry point

One person per team, update ui/cli.py to print "Hello" to the terminal in the run() function. Run main.py and make sure you see "hello" printed to the terminal.
Commit and push your code. Since you have checked out the feature branch in step 2, you will be committing the code into the feature branch.
```
git add <FILE(S) YOU WANT TO COMMIT>
git commit -m 'adding interfaces for task tracker'
git push
```

### Step 4
As a team, divide up the work of implementing each use case (each teammate should get at least one use case). Additionally, divide up the work of implemeting the files in `persistence/`, and `ui/`.

Document who will work on what file(s) below:
* Name - files
* Name - files
* Name - files

Commit your changes to the README.md file and push them.

### Step 5
Individually, everyone run `git pull` to update your feature_1 branch. Create another branch for your individual work (that branches off feature_1):
```
git branch <YOUR_BRANCH_NAME>
git checkout <YOUR_BRANCH_NAME>
```
Replace <YOUR_BRANCH_NAME> with some meaningful name. Don't use your name, instead, use the name of the file you'll be implementing. For example `cli` or `add_task`.

In your branch, implement the code in your assigned file. Feel free to use GenAI here liberally to speed up the process. Review GenAI generated code.  When you are finished, commit and push your code:
```
git add <FILES YOU WANT TO STAGE FOR COMMIT>
git commit -m 'added implementation for YOUR_FILE'
git push --set-upstream origin <YOUR_BRANCH_NAME>
```

This makes your branch available in the remote repository (in your team GitHub repository).

### Step 6
Individually, create a pull request from your branch to feature_1 branch. This pull request is a request to merge your changes to feature_1. To do this:
1. Go to your team GitHub repository
1. Go to the Pull requests menu. ![Pull Request Menu](docs/pull_request.png)
1. Click on the "New pull request" button. ![PR Button](docs/new_pull_request.png)
1. Select your branch as the source and feature_1 as destination of this PR. ![PR Source and Destination](docs/source_dest_of_pr.png)
1. Add a description of what this pull request accomplishes and how, submit hte PR. ![PR Description](docs/pr_description.png)
1. Look at 'Files changed' tab to review changes in a PR. ![PR changes](docs/files_changed.png)

### Step 7
As a team, review everyone's PR by opening each PR from the "Pull requests" menu and examining the details in the "Files changed". If any changes are needed, the author of the PR can commit and push the necessary changes to their branch. The PR will get updated with those changes automatically. 

### Step 8
If all the changes in the PR look acceptable, merge the PR using the "Merge pull request" button. ![Merge PR](docs/merge_pr.png)

### Step 9
Everyone, check out feature_1 branch
When everyone's PR has been merged to feature_1 branch, everyone check out feature_1 branch and pull the latest changes:
```
git checkout feature_1
git pull
```
From there, run  main.py and see if it works. There is a good chance that it won't work on the first try. 

### Step 10
If main.py doesn't work quite right, together figure out why and fix the problems. Commit and push all your changes to feature_1 branch.

### Step 11
When you get cli.py to work in feature_1 branch, have one person from your team create a pull request with feature_1 as the source and main as the destination. This process will be very similar to the process described in step 6.

## Connecting the Dots
Create a new branch to complete this final step. Add your answers into that branch, create a pull request, review it, and merge to main.

Your team just completed steps 0 through 11. Map those steps into the elements of our workflow, documented in this [GitHub Workflow Diagram](https://github.com/cse4504-wustl/workflow). Fill in the blanks below
* In class design in a feature branch: Steps ______
* Implement your part in YOUR branch made from feature branch: Steps ______
* In class review of your work: Steps ______
* Merge YOUR branch to feature branch: Steps ______
* Test feature branch: Steps ______
* Implement fixes in feature branch: Steps ______
* Merge feature branch to main: Steps ______

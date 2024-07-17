**Tasks Class Documentation**

Class Tasks
The Tasks class manages a collection of tasks, offering functionalities to read tasks from a file, manipulate them, and save changes back to the file.
Constructor (__init__ method)
Purpose: Initializes an instance of the Tasks class.
Attributes:

*tasks: List to store task details.*
Methods Called:
read(): Reads tasks from a file (Task.txt) during initialization.
Method read
Purpose: Reads task data from a file (Task.txt).
Parameters: None.
File Handling:
Opens Task.txt in read mode with UTF-8 encoding.
Splits file contents into parts based on '%'.
Splits each part into a list of task details (name, description, deadline, status).
Error Handling: Uses a try-finally block to ensure the file is closed properly.

*Method write*
Purpose: Writes current task data back to the file (Task.txt).
Parameters: None.
File Handling:
Opens Task.txt in write mode with UTF-8 encoding.
Constructs a string (concat) by concatenating task details, separated by commas.
Uses '%' to separate different tasks.
Error Handling: Uses a try-finally block to ensure the file is closed properly.

*Method inputTask*
Purpose: Allows user input to create a new task.
Parameters: None.
User Interaction:
Prompts the user to input task details (name, description, deadline, status).
Calls storeTask() to add the task to the tasks list and save changes to the file.

*Method storeTask*
Purpose: Adds a new task to the tasks list and saves changes to the file.
Parameters:
task_list: List containing task details (name, description, deadline, status).

*Method update*
Purpose: Updates an existing task based on the task name provided.
Parameters:
search: Task name to search for and update.
User Interaction:
Prompts the user to input updated task details (name, description, deadline, status).
Modifies the task details in the tasks list and saves changes to the file.

*Method delete*
Purpose: Deletes an existing task based on the task name provided.
Parameters:
search: Task name to search for and delete.
User Interaction:
Removes the task from the tasks list and saves changes to the file if found.
Prints a message if no task matching the provided name is found.

*Method listTasks*
Purpose: Lists all tasks currently stored in the tasks list.
Parameters: None.
User Output:
Iterates through the tasks list and prints each task's details.

*Method searchFilter*
Purpose: Searches for a task by its name.
Parameters:
search: Task name to search for.
Returns:
Returns the task (as a list of details) if found.
Returns None if no task matching the provided name is found.

**Main Script Documentation**
Main Script
The main script interacts with the Tasks class to provide a menu-driven interface for users to manage tasks.

User Interface

Menu Options:

Option '1': Adds a new task by calling inputTask() on the task_manager instance.

Option '2': Updates an existing task by calling update() on the task_manager instance.

Option '3': Deletes a task by calling delete() on the task_manager instance.

Option '4': Lists all tasks by calling listTasks() on the task_manager instance.

Option '5': Writes changes to the file and exits the program.

Error Handling
Invalid Option Handling: Prints an error message if the user enters an invalid menu option.
File Handling

Persistence: Ensures task data is persisted by saving changes to Task.txt after each operation.

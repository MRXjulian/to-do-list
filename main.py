from tasks import Tasks

task_manager = Tasks()

while True:
    print("Add Task -> 1\n"+
          "Update Task -> 2\n"+
          "Delete Task -> 3\n"+
          "List Tasks -> 4\n"+
          "Exit -> 5\n")
    option = input("Choose an option: ")
    
    if option == '1':
        task_manager.inputTask()
    elif option == '2':
        task_manager.update(input("Enter task name: "))
    elif option == '3':
        task_manager.delete(input("Enter the task to delete: "))
    elif option == '4':
        task_manager.listTasks()
    elif option == '5':
        task_manager.write()
        print("------ Goodbye ------")
        break
    else:
        print("That option doesn't exist :/")

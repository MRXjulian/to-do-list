class Tasks:
    
    def __init__(self):
        self.tasks = []
        self.read()
    
    ## Read the file
    def read(self):
        f = open("Task.txt", "r", encoding='utf-8')
        try:
            # split() returns a list
            parts = f.read().split('%')
            for part in parts:
                self.tasks.append(part.split(','))
        finally:
            f.close()
    
    # Write to the file
    def write(self):
        file = open("Task.txt", "w", encoding='utf-8')
        
        # Concatenate all values in the list into a string,
        # separated by a comma
        concat = " "
        last_index = len(self.tasks)
        for task in self.tasks:
            if last_index == 1:
                concat += ','.join(task)
            else:
                concat += ','.join(task) + "%"
            
            last_index -= 1
        
        try:
            file.write(concat)
        finally:
            file.close()
    
    def inputTask(self):
        print("--- Hello user, you are going to enter tasks ---")
        name = input("Name=> ")
        description = input("Description=> ")
        deadline = input("Deadline=> ")
        status = input("Status=> ")
        
        task_list = [name, description, deadline, status]
        self.storeTask(task_list)
    
    def storeTask(self, task_list):
        self.tasks.append(task_list)
        self.write()
    
    def update(self, search):
        found_task = self.searchFilter(search)
        if found_task is not None:
            print("-- UPDATE --")
            found_task[0] = input("name -> ")
            found_task[1] = input("description -> ")
            found_task[2] = input("deadline -> ")
            found_task[3] = input("status -> ")
            print("✅ Modified ✅")
            self.write()
        else:
            print("\nNo such item found.")
            print("\n---- These are the existing tasks ----")
            for task in self.tasks:
                print(task[0] + "\r")
    
    def delete(self, search):
        found_task = self.searchFilter(search)
        if found_task is not None:
            print("-- DELETE --")
            self.tasks.remove(found_task)
            print("✅ Deleted ✅")
        else:
            print("\nNo such item found.")
            print("\n---- These are the existing tasks ----")
            for task in self.tasks:
                print(task[0] + "\r")
    
    def listTasks(self):
        for task in self.tasks:
            print(task)
    
    def searchFilter(self, search):
        for task in self.tasks:
            if task[0] == search:
                return task
        
        return None

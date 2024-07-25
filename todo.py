def main():
    tasks = []

    while True:
        print("\n----My ToDo List-------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':
            print()
            n_task = int(input("How many tasks to add: "))


            for i in range(n_task):
                task=input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added successfully\n","All the best" ) 


        elif choice == '2':
            print("\nTasks:")
            for index , task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice =='3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("congratulations... you have completed your task")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exit My To Do List.")
            break

        else:
            print("Invalid Choice.. Please try again.")

if __name__ == "__main__":
    main()

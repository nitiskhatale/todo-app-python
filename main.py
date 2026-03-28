todo = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        task = input("enter your task: ")
        todo.append(task)
        print("Task Added:", task)

    elif choice == "2":
        if todo == []:
            print("no tasks available")
        else:
            number = 1
            for task in todo:
                print(number, ".", task)
                number += 1

    elif choice == "3":
        if todo == []:
            print("no tasks available")
        else:
            number = 1
            for task in todo:
                print(number, ".", task)
                number += 1

            delete_num = int(input("enter task number to delete: "))
            index = delete_num - 1

            if 0 <= index < len(todo):
                removed = todo.pop(index)
                print("Deleted:", removed)
            else:
                print("invalid number")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("invalid choice")

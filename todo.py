todo = []

task = True
print("Enter a task to complete")
print("If you want to quit, type 'quit'")
print("If you want to delete a task, type the task you would like to delete.")
while task:
    userInput = input("Task: ")
    if userInput.lower() == "delete":
        inputDelete = input("Type the task you would like to delete, type 'nothing' if you don't want to delete anything: ")
        if inputDelete == "nothing":
            continue
        for i in todo:
            if i == inputDelete:
                todo.remove(i)
                continue
        print(todo)
        continue
    if userInput.lower() == 'quit':
        task = False
        print(todo)
        break
    todo.append(userInput)
    print(todo)




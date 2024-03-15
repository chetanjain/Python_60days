# Add Edit feature
todos = []
while True:
    user_action = input("Type add , show , edit , complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        # with command helps to remove closing the file
        with open("../todo.txt", 'r') as file:
            todos = file.readlines()
        todos.append(todo+"\n")
        with open("../todo.txt", 'w') as file:  # r-> read, w-> write , a-> append
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open("../todo.txt", 'r') as file:
            todos = file.readlines()
        # print("todos : ", todos)
        # option 1 ------------------------------------------------------
        # todos = [x.replace('\n', '') for x in todos]
        # option 2 ------------------------------------------------------
        # todos = [x.strip('\n') for x in todos]
        # print(data)

        for index, todo in enumerate(todos):
            # print(index, '.', todo)  # improve this output as it comes 1 . clean
            # we will use f-string
            # option 3 ------------------------------------------------------
            todo = todo.strip('\n')
            print(f"{index + 1}. {todo}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            with open("../todo.txt", 'r') as file:
                todos = file.readlines()
            print(todos)
            # number = int(input("Number of todo to edit? : "))
            string = input("Enter the new todo for index :")
            todos[number - 1] = string + "\n"
            with open('../todo.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):  # modify the list, if user choose complete
        try:
            number = int(user_action.replace('complete', '').strip())
            with open("../todo.txt", 'r') as file:
                todos = file.readlines()
            # remove() is used to remove by value
            # pop is used to remove by index
            # number = int(input("Number of the todo to complete/remove"))
            todos.pop(number - 1)
            print(f"new todos: {todos}")
            with open("../todo.txt", 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("Please enter a valid index")
    elif user_action.startswith("exit"):
        print('bye')
        break
    else:
        print("Hey, you entered an incorrect request")

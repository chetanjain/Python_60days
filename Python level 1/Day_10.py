# Add Custom Functions
def get_todos():
    with open("../todo.txt", 'r') as file1:
        return file1.readlines()


while True:
    user_action = input("Type add , show , edit , complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        todos = get_todos()
        todos.append(todo + "\n")
        with open("../todo.txt", 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        for index, todo in enumerate(todos):

            todo = todo.strip('\n')
            print(f"{index + 1}. {todo}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos()
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
            todos = get_todos()
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

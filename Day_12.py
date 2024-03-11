# Default parameters, Adding docstring
def get_todos(filepath='todo.txt'):
    """
    Return the list of items in the file
    """
    with open(filepath, 'r') as file1:
        return file1.readlines()


#print(help(get_todos))


def write_todos(todos_arg, filepath='todos.txt', ):
    """
    :param todos_arg:
    :param filepath:
    :return: Nothing
    """
    with open(filepath, 'w') as file1:
        file1.writelines(todos_arg)


while True:
    user_action = input("Type add , show , edit , complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos_arg=todos)
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
            write_todos(todos_arg=todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):  # modify the list, if user choose complete
        try:
            number = int(user_action.replace('complete', '').strip())
            todos = get_todos()
            todos.pop(number - 1)
            print(f"new todos: {todos}")
            write_todos(todos_arg=todos)
        except IndexError:
            print("Please enter a valid index")
    elif user_action.startswith("exit"):
        print('bye')
        break
    else:
        print("Hey, you entered an incorrect request")

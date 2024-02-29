todos = []
while True:
    user_action = input("Type add , show or exit:")

    match user_action:
        case 'add':
            todo = input("Enter a todo:").strip()
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'exit':
            print('bye')
            break
        case _:  # _ means whatever value if we are putting
            print("Hey, you entered an incorrect request")

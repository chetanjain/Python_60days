# Add Edit feature
todos = []
while True:
    user_action = input("Type add , show , edit or exit:")

    match user_action:
        case 'add':
            todo = input("Enter a todo:").strip()
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'edit':
            for todo in todos:
                print(todo)
            number = int(input("Number of todo to edit? Index starts from 0: "))
            string = input("Enter the new todo for index :")
            todos[number]=string
            print("The New list will be:")
            for todo in todos:
                print(todo)
        case 'exit':
            print('bye')
            break
        case _:  # _ means whatever value if we are putting
            print("Hey, you entered an incorrect request")

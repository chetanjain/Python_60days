# Add Edit feature
todos = []
while True:
    user_action = input("Type add , show , edit , complete or exit:")

    match user_action:
        case 'add':
            todo = input("Enter a todo:").strip() + "\n"
            todos.append(todo)
            file = open('todo.txt', mode='a')  # r-> read, w-> write , a-> append
            file.writelines(todo)
            file.close()
        case 'show':
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()
            print("todos : ", todos)    
            for index, todo in enumerate(todos):
                # print(index, '.', todo)  # improve this output as it comes 1 . clean
                # we will use f-string
                print(f"{index + 1}. {todo}")
        case 'edit':
            for todo in todos:
                print(todo)
            number = int(input("Number of todo to edit? : "))
            string = input("Enter the new todo for index :")
            todos[number - 1] = string
            print("The New list will be:")
            for todo in todos:
                print(todo)
        case 'complete':  # modify the list, if user choose complete
            # remove() is used to remove by value
            # pop is used to remove by index
            number = int(input("Number of the todo to complete"))
            todos.pop(number + 1)
        case 'exit':
            print('bye')
            break
        case _:  # _ means whatever value if we are putting
            print("Hey, you entered an incorrect request")

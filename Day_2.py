# user_prompt = "Enter a todo:
# data_store = []
# todo1 = input("Enter a todo1:")
# data_store.append(todo1)
# todo2 = input("Enter a todo2:")
# data_store.append(todo2)
# todo3 = input("Enter a todo3:")
# data_store.append(todo3)
# print(data_store)
# ######################
# data = input("Enter Title")
# length = len(data)
# print("Title length is : ", length)
# ######################
user_prompt = "Enter a todo:"
too = []
while True:
    todo = input(user_prompt)
    too.append(todo.capitalize())
    print(too)

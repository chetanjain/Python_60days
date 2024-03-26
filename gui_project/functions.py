# Default parameters, Adding docstring
def get_todos(filepath='todo.txt'):
    """
    Return the list of items in the file
    """
    # print(get_todos.__doc__)
    with open(filepath, 'r') as file1:
        return file1.readlines()


def write_todos(todos_arg, filepath='todo.txt'):
    """
    :param todos_arg:
    :param filepath:
    :return: Nothing
    """
    with open(filepath, 'w') as file1:
        file1.writelines(todos_arg)


print(__name__,"hel")
if __name__ == "__main__":  # __name__ is variable which has default value as __main__
    # this __main__ value comes if you directly execute the current python file.
    print("Hello from functions")
    print(get_todos())

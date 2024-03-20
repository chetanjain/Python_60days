import functions
import PySimpleGUI as psg

print(__name__)

label = psg.Text("Type in a a To-Do")
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
add_button = psg.Button("Add")

list_box = psg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")

window = psg.Window(title="My To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 16))
# square bracket depicts new line
# the variables defined inside must be an object of PySimpleGUI
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos('todo.txt')
            new_todo = values['to-do'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos, 'todo.txt')
            window['todos'].update(values=todos)
        case psg.WINDOW_CLOSED:
            break
        case "Edit":
            todo_do_edit = values['todos'][0]
            new_todo = values['to-do'] + "\n"
            todos = functions.get_todos('todo.txt')
            edit_index = todos.index(todo_do_edit)
            todos[edit_index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['to-do'].update(value=values['todos'][0])
window.close()

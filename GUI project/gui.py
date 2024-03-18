import functions
import PySimpleGUI as psg

label = psg.Text("Type in a a To-Do")
input_box = psg.InputText(tooltip="Enter to-do", key="to-do")
add_button = psg.Button("Add")

window = psg.Window(title="My To-Do App",
                    layout=[[label], [input_box, add_button]],
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
        case psg.WINDOW_CLOSED:
            break
window.close()


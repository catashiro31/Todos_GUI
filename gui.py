import functions
import FreeSimpleGUI as sg
import time
import os
if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
sg.theme("DarkBrown1")
clock = sg.Text('',key="time_cur")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size= (45,10))
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
window = sg.Window("My To-do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica",14))

while True:
    event, values = window.read(timeout=10)
    match event:
        case sg.WIN_CLOSED | "Exit":
            break
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].strip('\n') + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].strip('\n') + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",14),title="Error")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todo(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",14),title="Error")
        case "todos":
            if len(values["todos"]):
                window["todo"].update(values["todos"][0])
    now = time.strftime("%b %d, %y %H:%M:%S")
    window["time_cur"].update(now)
window.close()
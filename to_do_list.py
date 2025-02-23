import PySimpleGUI as sg

tasks = ["something", "something2", "something3"]

layout = [
    [sg.Text('ToDo')],
    [sg.InputText('Enter ToDo Task', key='todo_task'), sg.Button(button_text='Add', key="add_save")],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Edit')],
]

window = sg.Window('ToDo App', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
    elif event == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
    elif event == None:
        break

window.Close()

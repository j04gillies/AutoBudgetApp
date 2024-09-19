import PySimpleGUI as sg

#Layout
layout = [ [sg.Text("Auto Budget App")],
          [sg.Text("Enter something on Row 2"), sg.InputText()],
          [sg.Button("Ok"), sg.Button("Cancel")]]

window = sg.Window("Auto Budget", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    print("You entered", values[0])

window.close()
import PySimpleGUI as sg

def get_user_inputs():
    layout = [
        [sg.OptionMenu(["Expense","Income","Save"],key="recordtype")],
        [sg.Text("Enter label:"), sg.Input(key="label")],
        [sg.Text("Enter value:"), sg.Input(key="value")],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]

    window = sg.Window("Add a record",layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Submit":
            #begin input validation
            try:
                value = float(values["value"])
                if value < 0:
                    sg.popup("Please input a value above 0",title="Input Error")
                    continue
            except ValueError:
                sg.popup("Please enter a valid integer for value.",title="Input Error")
                continue

            window.close()
            return values
    window.close()
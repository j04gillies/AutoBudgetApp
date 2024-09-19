import PySimpleGUI as sg
import recordInput

all_user_inputs = [] #List to store all records


#Layout
layout = [ [sg.Text("Auto Budget App",font="Any 15",justification='center',expand_x=True)],
          [sg.Button("Add Records",key="-AddRecord-"),sg.Button("List Records",key="-ListRecords-")]]

window = sg.Window("Auto Budget App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    if event == "-AddRecord-":
        userInput = recordInput.get_user_inputs()
        print("Added a record.")

        if userInput:
            all_user_inputs.append(userInput)
            
    if event == "-ListRecords-":
        for i,inputs in enumerate(all_user_inputs,0):
            label, recordtype, value = inputs
            print(f"Label: {label}, type: {recordtype}, value: {value}")
            

window.close()
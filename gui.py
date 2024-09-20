import PySimpleGUI as sg
import recordInput
import functions
import os

all_user_inputs = []  # List to store all records

# Load existing records from file
if os.path.isfile("records.json"):
    all_user_inputs = functions.retrieve_saved_records()  # Call the function, not append it

#Table 1
tb_headings = ["Type","Label","Value"]

#Layout
layout = [ [sg.Text("Auto Budget App",font="Any 15",justification='center',expand_x=True)],
          [sg.Table(values=all_user_inputs, headings=tb_headings, key="-TABLE-", expand_x=True)],
          [sg.Button("Add Records",key="-AddRecord-"),sg.Button("Clear Saved",key="-ClearSaved-")]]

window = sg.Window("Auto Budget App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        functions.save_records_to_file(all_user_inputs)
        break
    if event == "-AddRecord-":
        userInput = recordInput.get_user_inputs()
        print("Added a record.")

        if userInput:
            all_user_inputs.append(userInput)
            functions.save_records_to_file(all_user_inputs)
            window["-TABLE-"].update(values=all_user_inputs)
            window.refresh()
    
    if event == "-ClearSaved-":
        all_user_inputs.clear()
        window["-TABLE-"].update(values=all_user_inputs)
        window.refresh()
            

window.close()
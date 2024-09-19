import PySimpleGUI as sg
import recordInput
import functions
import os

all_user_inputs = []  # List to store all records

# Load existing records from file
if os.path.isfile("records.json"):
    all_user_inputs = functions.retrieve_saved_records()  # Call the function, not append it

#Layout
layout = [ [sg.Text("Auto Budget App",font="Any 15",justification='center',expand_x=True)],
          [sg.Button("Add Records",key="-AddRecord-"),sg.Button("List Records",key="-ListRecords-"),sg.Button("")]]

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
            functions.save_records_to_file(all_user_inputs)

    if event == "-ListRecords-":
        if all_user_inputs:
            for i,inputs in enumerate(all_user_inputs,1):
                label, recordtype, value = inputs
                print(f"Label: {label}, type: {recordtype}, value: {value}")
        else:
            print("No records to list.")
            

window.close()
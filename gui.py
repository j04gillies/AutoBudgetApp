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
tbl1 = sg.Table(values=all_user_inputs, 
                headings=tb_headings, key="-TABLE-", 
                expand_x=True,
                expand_y=True,
                justification="center",                
                enable_events=True,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE)

#Layout
layout = [[sg.Text("Auto Budget App",font="Any 15",justification='center',expand_x=True)],
          [tbl1],
          [sg.Button("Add Records",key="-AddRecord-"),
           sg.Button("Clear Saved",key="-ClearSaved-"),
           sg.Button("Remove Line",key="-Remove-"),
           sg.Button("Sort",key="-Sort-")],
           [sg.Button("Display Budget", key="-DisplayBudget-",expand_x=True)]]

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
    
    if event == "-Sort-":
        all_user_inputs = functions.sort_records(all_user_inputs)
        window["-TABLE-"].update(values=all_user_inputs)
        window.refresh()
    
    if event == "-Remove-":
        selected_rows = values["-TABLE-"]

        if selected_rows:
            selected_index = selected_rows[0]
            del all_user_inputs[selected_index]
            window["-TABLE-"].update(values=all_user_inputs)
            functions.save_records_to_file(all_user_inputs)
        else:
            sg.popup("Please select a row to remove.", title="No Selection Error")
            

window.close()
import PySimpleGUI as sg
import functions

def displayBudget(budget_records):
    layout = [
        [sg.Text("Budget",font="Any 15",justification='center',expand_x=True)],
    ]
    income, expense, save = functions.calculate_saving(budget_records)

    print("Income = ", str(income))
    print("Expense = ",str(expense))
    print("You can save",str(income - expense))

    window = sg.Window("Budget", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        
    window.close()
    return None
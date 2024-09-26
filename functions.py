import json

def save_records_to_file(data):
    with open("records.json", "w") as file:
        json.dump(data, file)  # Use `with` to ensure the file is properly closed

def retrieve_saved_records():
    try:
        with open("records.json", "r") as file:
            return json.load(file)  # Properly read the file and return the JSON data
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # If the file is not found or empty, return an empty list
    
def sort_records(data):
    income = []
    expense = []
    save = []
    for x in data:
        if x[0] == "Income":
            income.append(x)
        elif x[0] == "Expense":
            expense.append(x)
        else:
            save.append(x)
    return income + expense + save
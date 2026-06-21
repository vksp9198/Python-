import json

def total_spending(Expenses):
    total = 0
    for key, data in Expenses.items():
        # print(f"{key} : ₹{data["Amount"]}")
        total += data["Amount"]
    print("-" *40)
    print(f"Total Spending : ₹{total}")

def search_expense(Expenses):
    category = input("Enter category name to search : ").strip()
    if category in Expenses:
        for key,data in Expenses.items():
            if category == key:
                print("-" *40)
                print(f"{key} : ₹{data["Amount"]}")
    else:
        print("Categroy name NOT found!!")
    
def delete_expense(Expenses):
    view_expense(Expenses)
    category = input("Enter category name to delete : ").strip()
    if category in Expenses:
        del Expenses[category]
        print("-" *40)
        print(f"Category deleted successfully!")
    else:
        print("-" *40)
        print("Wrong categroy name!!")
    save_data(Expenses)
    print("-" *80)

def view_expense(Expenses):
    load_data()
    # print(type(Expenses))
    # print(Expenses)
    print("-" *20 ,"All Expenses","-" *20)
    for key, data in Expenses.items():
        print(f"{key} : ₹{data["Amount"]}")
        
    print("-" *40)
    
def add_expense(Expenses):
    category = input("Enter category name : ").strip()
    amount = float(input("Enter amount : "))

    Expenses[category] = {
            "Amount" : amount
        }
    
    print("-" *10 ,"Expense Added successfully!!","-" *10)
    save_data(Expenses)
    # print(Expenses)

def save_data(Expenses):
    # print(Expenses)
    with open("expense_data.json", "w") as file:
        json.dump(Expenses,file , indent=4)
    # print("Data saved successfully!")

def load_data():
    try:
        with open("expense_data.json" , "r") as file:
            # print(file.read())
            Expenses = json.load(file)
            return Expenses
    except (FileNotFoundError,json.JSONDecodeError):
        Expenses = {}
        print("File not found!! , create New one")
        return []
def main():
    Expenses = load_data()

    # {
    #     "food" : 250,
    #     "travel" : 700
    # }

    while True:
        print("===========EXPENSE TRACKER==========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Calculate Total Spending")
        print("6. Exit")

        choice = input("Enter your choice : ")
        match choice:
            case '1' : add_expense(Expenses)
            case '2' : view_expense(Expenses)
            case '3' : delete_expense(Expenses)
            case '4' : search_expense(Expenses)
            case '5' : total_spending(Expenses)
            case '6' : 
                print("Goodbye!!")
                break

if __name__ == "__main__":
    main()
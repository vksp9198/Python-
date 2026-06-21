
Expenses = {}

category = input("Category")
amount = input("amount")

Expenses[category] = {
        "Amount" : amount
    }

print(type(Expenses))
print(Expenses)
print(Expenses[category])
# print(Expenses[Amount])
for key , data in Expenses.items():
    if category == key:
        print(f"{key} : {data["Amount"]}")
    else:
        print("No")

        


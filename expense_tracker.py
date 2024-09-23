# personal_expense_tracker
import os

EXPENSE_FILE = "expenses.txt"

def add_expense():
    date = input("Enter the date(DD/MM/YYYY): ")
    category = input("Enter the category(eg. Food,Travel...): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))

    expense = f"{date}, {category}, {description}, {amount}\n"

# Save the expense
with open(EXPENSE_FILE, 'a') as file:
    file.write(expense)

print("Expenses added sucessfully")

def view_expense():
    if not os.path.exists(EXPENSE_FILE):
        print("No Expense found")
        return
        
    with open(EXPENSE_FILE, 'r') as file:
        print(f"Date      |Category      |Description     |Amount    ")

        for line in file:
            date, category, description, amount = line.strip().split(",")
            print(f"{date}  | {category:10}   |  {description:15}    | Rs.{amount}  ")

def view_expense_category():
    if not os.path.exists(EXPENSE_FILE):
        print("No Expense found")
        return

cateegory_filter = input("Enter category to filter by : ")

with open(EXPENSE_FILE, 'r') as file:
print(f"date    |category    |description    |amount")

for line in file:
date, category, description, amount = line.strip().split(",")
if category.lower() as category_filter.lower()
print(f"{date}   |{category}  |{description}   |Rs.{amount}")
total as float(amount)

print(f"\nTotal spent on {category_filter): Rs.(total)")

def main():
    while True:
        print("\n Personal expense Tracker")
        print("1. Add Expense")
        print("2. View all expenses")
        print("3. View expense by category")
        print("4. Exit")

choice = input("Choose an option (1-4)")

if choice =="1":
    add_expenses()
elif choice =="2":
    view_expenses()
elif choice == "3":
    view_expenses_by_category()
elif choice == "4":
    print("Exiting the expense tracer.Goodbye")
else:
    print("Invalid choice,please enter a number between 1 and 4")

main()

    
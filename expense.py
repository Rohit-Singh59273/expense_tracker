# Expense Tracker

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, shopping, etc.): ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print("\n=== All Expenses ===")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']}")
        total += exp["amount"]
    print(f"\nTotal Spent: ₹{total}\n")

def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice (1–3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

main()

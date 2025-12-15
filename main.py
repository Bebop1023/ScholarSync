from core.expenses import add_expense, load_expenses

def show_menu():
    print("ScholarSync Expense Tracker")
    print("1. Log Expense")
    print("2. View Expenses")
    print("0. Exit")

def log_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        note = input("Enter a note (optional): ")
        add_expense(amount, category, note)
        print("Expense logged successfully.")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("Recorded Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} - {expense['category']}: ${expense['amount']} ({expense['note']})")
    
def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            log_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "0":
            print("Exiting ScholarSync Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
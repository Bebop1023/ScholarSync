from core.expenses import add_expense, load_expenses, get_expense_summary

from core.habits import (
    create_habit,
    complete_habit,
    load_habits,
    calculate_streak
)

def show_menu():
    print("ScholarSync Expense Tracker")
    print("1. Log Expense")
    print("2. View Expenses")
    print("3. View Expense Summary")
    print("4. Create Habit")
    print("5. Complete Habit")
    print("6. View Habits")
    print("0. Exit")

def log_expense():
    try:
        raw_amount = input("Enter amount (e.g. 12.50 or $12.50): ")
        cleaned_amount = raw_amount.replace("$", "").strip()
        amount = float(cleaned_amount)

        category = input("Enter category (Food, Transport, etc): ")
        note = input("Optional note: ")

        add_expense(amount, category, note)
        print("✅ Expense saved.")

    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")



def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("Recorded Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} - {expense['category']}: ${expense['amount']} ({expense['note']})")


def view_summary():
    summary = get_expense_summary()

    print("\n--- Expense Summary ---")
    print(f"Total spent: ${summary['total']:.2f}")

    print("\nBy Category:")
    for category, amount in summary["by_category"].items():
        print(f"- {category}: ${amount:.2f}")

def create_habit():
    name = input("Enter habit name: ")
    frequency = input("Enter frequency (daily, weekly): ")
    create_habit(name, frequency)
    print("✅ Habit created.")

def complete_habit():
    name = input("Enter habit name to complete: ")
    complete_habit(name)
    print("✅ Habit completed.")

def view_habits():
    habits = load_habits()
    if not habits:
        print("No habits recorded.")
        return
    for habit in habits:
        streak = calculate_streak(habit["name"])
        print(f"- {habit['name']} ({habit['frequency']}) | Streak: {streak}")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            log_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "4":
            create_habit()
        elif choice == "5":
            complete_habit()
        elif choice == "6":
            view_habits()
        elif choice == "0":
            print("Exiting ScholarSync Expense Tracker.")
        elif choice == "3":
            view_summary()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
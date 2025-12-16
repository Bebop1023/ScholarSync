from core.expenses import add_expense, load_expenses, get_expense_summary
from core.habits import (
    create_habit as create_habit_logic,
    complete_habit,
    load_habits,
    calculate_streak
)


def show_menu():
    print("\n=== ScholarSync ===")
    print("1. Log Expense")
    print("2. View Expenses")
    print("3. View Expense Summary")
    print("4. Create Habit")
    print("5. Complete Habit")
    print("6. View Habits")
    print("0. Exit")


# -------------------- EXPENSES --------------------

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
        print("No expenses recorded yet.")
        return

    print("\n--- Expenses ---")
    for exp in expenses:
        print(f"{exp['date']} | ${exp['amount']:.2f} | {exp['category']} | {exp['note']}")


def view_summary():
    summary = get_expense_summary()

    print("\n--- Expense Summary ---")
    print(f"Total spent: ${summary['total']:.2f}")

    if not summary["by_category"]:
        print("No expenses yet.")
        return

    print("\nBy Category:")
    for category, amount in summary["by_category"].items():
        print(f"- {category}: ${amount:.2f}")


# -------------------- HABITS --------------------

def add_habit():
    name = input("Enter habit name: ")

    if create_habit_logic(name):
        print("✅ Habit created.")
    else:
        print("⚠️ Habit already exists.")


def mark_habit():
    name = input("Enter habit name to mark complete: ")

    if complete_habit(name):
        print("✅ Habit marked complete for today.")
    else:
        print("❌ Habit not found.")


def view_habits():
    habits = load_habits()

    if not habits:
        print("No habits created yet.")
        return

    print("\n--- Habits ---")
    for habit in habits:
        streak = calculate_streak(habit["completed_dates"])
        print(f"{habit['name']} | Streak: {streak} day(s)")


# -------------------- MAIN LOOP --------------------

def main():
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            add_habit()
        elif choice == "5":
            mark_habit()
        elif choice == "6":
            view_habits()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

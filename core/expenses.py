import json
from datetime import datetime
from pathlib import Path

#Path to the expenses data file
DATA_FILE = Path("data/expenses.json")

def load_expenses():
    """Load expenses from the JSON data file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    

def save_expenses(expenses):
    """Save expenses to the JSON data file."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(amount, category, note=""):
    """Add a new expense entry."""
    expenses = load_expenses()
    
    expense_entry = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": datetime.now().isoformat()
    }
    expenses.append(expense_entry)
    save_expenses(expenses)
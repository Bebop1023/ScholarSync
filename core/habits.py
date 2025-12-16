import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/habits.json")

def load_habits():
    """Load habits from the JSON data file."""
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def save_habits(habits):
    """Save habits to the JSON data file."""
    with open(DATA_FILE, "w") as file:
        json.dump(habits, file, indent=4)

def create_habit(name):
    """Create a new habit entry."""
    habits = load_habits()

    for habit in habits:
        if habit["name"].lower() == name.lower():
            return False  # Habit already exists
        
    habits.append({
        "name": name,
        "completed_dates": []
    })

    save_habits(habits)
    return True


def complete_habit(name):
    """Mark a habit as completed for today."""
    habits = load_habits()
    today = datetime.now().strftime("%Y-%m-%d")

    for habit in habits:
        if habit["name"].lower() == name.lower():
            if today not in habit["completed_dates"]:
                habit["completed_dates"].append(today)
                save_habits(habits)
                return True
            
    return False  # Already completed today


def calculate_streak(completed_dates):
    if not completed_dates:
        return 0

    completed = sorted(completed_dates, reverse=True)
    streak = 0
    today = datetime.now().strftime("%Y-%m-%d")

    current_date = today

    for date in completed:
        if date == current_date:
            streak += 1
            current_date = datetime.strptime(
                current_date, "%Y-%m-%d"
            ).replace(day=int(current_date[-2:]) - 1).strftime("%Y-%m-%d")
        else:
            break

    return streak
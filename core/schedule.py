import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/schedule.json")


def load_schedule():
    if not DATA_FILE.exists():
        return {"courses": [], "assignments": []}

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_schedule(schedule):
    with open(DATA_FILE, "w") as file:
        json.dump(schedule, file, indent=4)


def add_course(name, days, start_time, duration_minutes):
    schedule = load_schedule()

    schedule["courses"].append({
        "name": name,
        "days": days,
        "start_time": start_time,
        "duration_minutes": duration_minutes
    })

    save_schedule(schedule)



def add_assignment(course, title, due_date):
    schedule = load_schedule()

    schedule["assignments"].append({
        "course": course,
        "title": title,
        "due_date": due_date
    })

    save_schedule(schedule)


def get_upcoming_assignments():
    schedule = load_schedule()
    today = datetime.now().strftime("%Y-%m-%d")

    upcoming = []

    for assignment in schedule["assignments"]:
        if assignment["due_date"] >= today:
            upcoming.append(assignment)

    return sorted(upcoming, key=lambda x: x["due_date"])

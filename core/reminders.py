from datetime import datetime
from core.schedule import load_schedule


def get_assignment_reminders(days_ahead=2):
    schedule = load_schedule()
    today = datetime.now().date()

    reminders = []

    for assignment in schedule["assignments"]:
        due_date = datetime.strptime(
            assignment["due_date"], "%Y-%m-%d"
        ).date()

        days_until = (due_date - today).days

        if 0 <= days_until <= days_ahead:
            reminders.append(
                f"📌 {assignment['title']} for {assignment['course']} is due in {days_until} day(s)."
            )

    return reminders


def get_today_classes():
    schedule = load_schedule()
    today_day = datetime.now().strftime("%a")  # Mon, Tue, Wed

    reminders = []

    for course in schedule["courses"]:
        if today_day in course["days"]:
            reminders.append(
                f"📚 You have {course['name']} today at {course['start_time']}."
            )

    return reminders

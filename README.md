# ScholarSync

ScholarSync is a Python-based productivity app built for college students.
It combines expense tracking, habit tracking, class scheduling, reminders,
and an AI-powered advisor into one simple system.

I built this project to better understand how real applications are structured
beyond coursework, with a focus on clean code, modular design, and practical
features students actually need.

---

## What ScholarSync Does

- Track daily expenses and see where money is going
- Create habits and maintain streaks over time
- Store class schedules and assignment due dates
- Get reminders for upcoming deadlines and classes
- Receive personalized study and lifestyle advice using an LLM

The app runs as a command-line program but is designed in a way that could
easily scale into a web or mobile application.

---

## Features

### Expense Tracking
- Log expenses with categories and notes
- View total spending and category breakdowns

### Habit Tracking
- Create habits
- Mark habits as completed
- Automatically calculate streaks

### Scheduling
- Add courses with meeting days and times
- Add assignments with due dates
- View upcoming assignments

### Reminders
- Alerts for assignments due soon
- Alerts for classes happening today

### AI Advisor
- Analyzes expenses, habits, and workload
- Generates personalized, actionable advice
- Uses environment variables for secure API key handling

---

## Tech Used

- Python 3.11
- Modular project structure
- OpenAI API for AI advice
- JSON files for local data storage
- Git and GitHub for version control
- Virtual environments and dotenv for dependency and secret management

---

## Security Notes

- API keys are stored locally in a `.env` file
- `.env`, virtual environments, and cache files are ignored by Git
- GitHub secret scanning rules are respected

---

## Running the Project

Clone the repository:
```bash
git clone https://github.com/yourusername/ScholarSync.git
cd ScholarSync


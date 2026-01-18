from fastapi import FastAPI
from core.expenses import add_expense, load_expenses, get_expense_summary

app = FastAPI(title="ScholarSync API")


@app.get("/")
def root():
    return {"message": "ScholarSync API is running"}


@app.get("/expenses")
def get_expenses():
    return load_expenses()


@app.post("/expenses")
def create_expense(amount: float, category: str, note: str = ""):
    add_expense(amount, category, note)
    return {"status": "expense added"}


@app.get("/expenses/summary")
def expense_summary():
    return get_expense_summary()

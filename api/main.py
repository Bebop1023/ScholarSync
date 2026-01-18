from datetime import date as dt

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db.database import Base, engine, get_db
from db.models import Expense

app = FastAPI(title="ScholarSync API")

# Ensure tables exist (safe to call on startup)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "ScholarSync API is running"}


@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).order_by(Expense.id.desc()).all()
    return [
        {
            "id": e.id,
            "amount": e.amount,
            "category": e.category,
            "note": e.note,
            "date": e.date,
        }
        for e in expenses
    ]


@app.post("/expenses")
def create_expense(
    amount: float,
    category: str,
    note: str = "",
    date: str = "",
    db: Session = Depends(get_db),
):
    use_date = date or dt.today().isoformat()

    exp = Expense(
        amount=float(amount),
        category=category.strip(),
        note=note.strip(),
        date=use_date,
    )
    db.add(exp)
    db.commit()
    db.refresh(exp)

    return {
        "status": "expense added",
        "expense": {
            "id": exp.id,
            "amount": exp.amount,
            "category": exp.category,
            "note": exp.note,
            "date": exp.date,
        },
    }


@app.get("/expenses/summary")
def expense_summary(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()

    total = sum(e.amount for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e.category] = by_category.get(e.category, 0.0) + e.amount

    return {"total": total, "by_category": by_category}



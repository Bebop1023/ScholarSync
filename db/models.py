from sqlalchemy import Column, Integer, Float, String
from db.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    note = Column(String, default="")
    date = Column(String, nullable=False)  # keep as string for now (simple)

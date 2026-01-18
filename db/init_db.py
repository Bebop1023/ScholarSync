from db.database import Base, engine
from db import models  # noqa: F401 (ensures models are registered)

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
    print("Database tables created.")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with PostgreSQL URI in production
DATABASE_URL = "sqlite:///./test.db"  # For local dev/testing

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for route injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

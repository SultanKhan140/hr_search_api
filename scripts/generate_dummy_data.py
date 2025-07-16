import os
import sys
import random
from faker import Faker

# Ensure app/ folder is in the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import SessionLocal
from app.models.employee import Employee
from app.models.employee import Employee, Department, Position, Location, Organization ,ContactInfo


fake = Faker()

from app.db.session import engine
from app.db.session import Base
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def safe_add(db, model, field, values):
    existing = {getattr(x, field) for x in db.query(model).all()}
    for val in values:
        if val not in existing:
            db.add(model(**{field: val}))
    db.commit()

def seed_reference_data(db):
    safe_add(db, Department, "name", ["Engineering", "Marketing", "HR", "Finance", "Support"])
    safe_add(db, Position, "title", ["Manager", "Executive", "Intern", "Lead", "Analyst"])
    safe_add(db, Location, "city", ["London", "New York", "Berlin", "Bangalore", "Remote"])
    safe_add(db, Organization, "name", ["Acme Corp", "Globex", "Umbrella", "Wayne Enterprises", "Stark Industries"])

    return {
        "departments": db.query(Department).all(),
        "positions": db.query(Position).all(),
        "locations": db.query(Location).all(),
        "organizations": db.query(Organization).all(),
    }
def generate_employees(db, count=100):
    refs = seed_reference_data(db)

    statuses = ["Active", "Not started", "Terminated"]

    for _ in range(count):
        emp = Employee(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            status=random.choice(statuses),
            department=random.choice(refs["departments"]),
            position=random.choice(refs["positions"]),
            location=random.choice(refs["locations"]),
            organization=random.choice(refs["organizations"]),
        )
        db.add(emp)
        db.flush()  # get emp.id before adding contact info

        contact = ContactInfo(
            email=fake.email(),
            phone=fake.phone_number(),
            employee_id=emp.id
        )
        db.add(contact)

    db.commit()
    print(f"✅ Inserted {count} dummy employees with contact info.")


if __name__ == "__main__":
    db = SessionLocal()
    generate_employees(db)
    db.close()

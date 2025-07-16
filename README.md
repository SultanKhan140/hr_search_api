# 🧑‍💼 HR Employee Search API

A backend-only FastAPI microservice to search employee records with support for:
- Organization-based dynamic column visibility
- Advanced filtering (by department, location, position, status, etc.)
- Rate-limiting (custom, no external libraries)
- Soft deletion & timestamps
- Relational models for departments, positions, locations, contact info

---

## 🚀 Features

- 🔍 Search employees by:
  - Status (`ACTIVE`, `TERMINATED`, `NOT_STARTED`)
  - Department
  - Location
  - Position
  - Company (Organization)
- 🧠 Organization-specific **dynamic column rendering**
- 🧼 No data leaks across organizations
- 🧾 Auto-managed `created_at`, `updated_at`, and `is_deleted`
- 🚫 In-memory rate limiting (no external libraries)
- 🔄 Containerizable & testable backend

---

## 🧑‍💻 Tech Stack

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **ORM**: SQLAlchemy Core + ORM
- **Database**: SQLite (dev only) — replaceable with PostgreSQL
- **API Docs**: Swagger (auto-generated)

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/hr-search-api
cd hr-search-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Generate dummy data
python scripts/generate_dummy_data.py

# Run the API
uvicorn app.main:app --reload

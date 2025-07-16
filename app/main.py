from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes as search
from app.db.session import engine, Base

# Initialize the DB (optional for SQLite/demo)
def init_db():
    Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="HR Employee Search API",
    description="A backend-only FastAPI microservice for HR employee search directory.",
    version="1.0.0",
)

# Include your routers
app.include_router(search.router, prefix="/api", tags=["Search"])

# CORS Middleware (optional, for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB at startup (useful for SQLite or mock DB)
@app.on_event("startup")
def startup_event():
    init_db()

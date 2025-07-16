from fastapi import APIRouter, Query, Request, Depends ,HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.employee_search import search_employees
from app.core.dynamic_columns import get_allowed_columns
from app.core.rate_limiter import is_rate_limited

router = APIRouter()

@router.get("/search")
def search_api(
    request: Request,
    status: Optional[List[str]] = Query(default=None),
    location: Optional[str] = None,
    company: Optional[str] = None,
    department: Optional[str] = None,
    position: Optional[str] = None,
    db: Session = Depends(get_db),
):
    # Simple rate limiter
    client_id = request.client.host
    if is_rate_limited(client_id):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Assume fixed org_id for testing
    org_id = 2

    filters = {
        "status": status,
        "location": location,
        "company": company,
        "department": department,
        "position": position
    }

    employees = search_employees(filters=filters, org_id=org_id, db=db)
    return {
        "count": len(employees),
        "results": employees
    }


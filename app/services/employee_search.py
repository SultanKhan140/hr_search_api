from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing import Dict, List, Any
from app.models.employee import Employee, Department, Position, Location, Organization, ContactInfo
from app.core.dynamic_columns import get_allowed_columns


def search_employees(
    filters: Dict[str, Any],
    org_id: int,
    db
) -> List[Dict[str, Any]]:
    # 🎯 Get dynamic columns based on org ID
    columns = get_allowed_columns(org_id)

    # 🏗️ Query with joins
    stmt = (
        select(Employee)
        .join(Employee.department)
        .join(Employee.position)
        .join(Employee.location)
        .join(Employee.organization)
        .options(
            joinedload(Employee.department),
            joinedload(Employee.position),
            joinedload(Employee.location),
            joinedload(Employee.organization),
            joinedload(Employee.contact_info),
        )
        .filter(
            Employee.organization_id == org_id,
            Employee.is_deleted == False
        )
    )

    # 🎛️ Apply filters
    if status := filters.get("status"):
        stmt = stmt.filter(Employee.status.in_(status))
    if location := filters.get("location"):
        stmt = stmt.filter(Location.city == location)
    if department := filters.get("department"):
        stmt = stmt.filter(Department.name == department)
    if position := filters.get("position"):
        stmt = stmt.filter(Position.title == position)
    if company := filters.get("company"):
        stmt = stmt.filter(Organization.name == company)

    # 🚀 Fetch results
    employees = db.execute(stmt).scalars().all()

    # 🧾 Serialize
    def serialize(emp: Employee) -> Dict[str, Any]:
        return {
            col: (
                emp.department.name if col == "department" else
                emp.position.title if col == "position" else
                emp.location.city if col == "location" else
                emp.organization.name if col in {"organization", "company"} else
                {
                    "email": emp.contact_info.email if emp.contact_info else None,
                    "phone": emp.contact_info.phone if emp.contact_info else None
                } if col == "contact_info" else
                getattr(emp, col, None)
            )
            for col in columns
        }

    return [serialize(emp) for emp in employees]
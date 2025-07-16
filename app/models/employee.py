from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.models.base import BaseModelMixin

class Department(Base, BaseModelMixin):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Position(Base, BaseModelMixin):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)

class Location(Base, BaseModelMixin):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, unique=True, index=True)

class Organization(Base, BaseModelMixin):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class ContactInfo(Base, BaseModelMixin):
    __tablename__ = "contact_infos"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))

    employee = relationship("Employee", back_populates="contact_info")

class Employee(Base, BaseModelMixin):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    status = Column(String, index=True)

    department_id = Column(Integer, ForeignKey("departments.id"))
    position_id = Column(Integer, ForeignKey("positions.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    department = relationship("Department")
    position = relationship("Position")
    location = relationship("Location")
    organization = relationship("Organization")
    contact_info = relationship("ContactInfo", uselist=False, back_populates="employee")

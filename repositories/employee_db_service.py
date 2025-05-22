from sqlalchemy.orm import Session
from typing import List, Optional

from models.employee_model import Employee
from schema.employee_schema import EmployeeCreate

def create_employee(db: Session, employee: EmployeeCreate) -> Employee:
    db_employee = Employee(**employee.dict(exclude_unset=True))
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee_by_id(db: Session, employee_id: int) -> Optional[Employee]:
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()

def get_all_employees(db: Session, skip: int = 0, limit: int = 100) -> List[Employee]:
    return db.query(Employee).offset(skip).limit(limit).all()

def update_employee(db: Session, employee_id: int, employee_update: EmployeeCreate) -> Optional[Employee]:
    db_employee = get_employee_by_id(db, employee_id)
    if not db_employee:
        return None
    for key, value in employee_update.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int) -> bool:
    db_employee = get_employee_by_id(db, employee_id)
    if not db_employee:
        return False
    db.delete(db_employee)
    db.commit()
    return True

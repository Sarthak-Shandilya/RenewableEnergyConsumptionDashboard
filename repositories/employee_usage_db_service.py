from sqlalchemy.orm import Session
from typing import List, Optional

from models.employee_usage_model import EmployeeUsage
from schema.employee_usage_schema import EmployeeUsageCreate, EmployeeUsageUpdate


def create_employee_usage(db: Session, usage: EmployeeUsageCreate) -> EmployeeUsage:
    db_usage = EmployeeUsage(**usage.dict(exclude_unset=True))
    db.add(db_usage)
    db.commit()
    db.refresh(db_usage)
    return db_usage


def get_employee_usage_by_id(db: Session, emission_id: int) -> Optional[EmployeeUsage]:
    return db.query(EmployeeUsage).filter(EmployeeUsage.emission_id == emission_id).first()


def get_all_employee_usages(db: Session, skip: int = 0, limit: int = 100) -> List[EmployeeUsage]:
    return db.query(EmployeeUsage).offset(skip).limit(limit).all()


def update_employee_usage(db: Session, emission_id: int, usage_update: EmployeeUsageUpdate) -> Optional[EmployeeUsage]:
    db_usage = get_employee_usage_by_id(db, emission_id)
    if not db_usage:
        return None
    for key, value in usage_update.dict(exclude_unset=True).items():
        setattr(db_usage, key, value)
    db.commit()
    db.refresh(db_usage)
    return db_usage


def delete_employee_usage(db: Session, emission_id: int) -> bool:
    db_usage = get_employee_usage_by_id(db, emission_id)
    if not db_usage:
        return False
    db.delete(db_usage)
    db.commit()
    return True

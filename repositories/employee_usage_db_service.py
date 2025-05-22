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


def get_usage_by_employee(db: Session, employee_id: int):
    return db.query(EmployeeUsage).filter(EmployeeUsage.employee_id == employee_id).all()

def calculate_energy(duration: int, dark_mode: bool) -> float:
    # Example: Base consumption is 0.05 kWh per 10 mins
    base_rate = 0.005
    if dark_mode:
        base_rate *= 0.7  # 30% savings in dark mode
    return round(duration * base_rate, 4)

def create_usage_entry(db: Session, usage: EmployeeUsageCreate):
    energy = calculate_energy(usage.battery_usage, usage.dark_mode)
    db_usage = EmployeeUsage(
        employee_id=usage.employee_id,
        battery_usage=usage.battery_usage,
        dark_mode=usage.dark_mode,
        energy_used_kwh=energy
    )
    db.add(db_usage)
    db.commit()
    db.refresh(db_usage)
    return db_usage

def get_employee_usages(db: Session, employee_id: int):
    return db.query(EmployeeUsage).filter(EmployeeUsage.employee_id == employee_id).all()
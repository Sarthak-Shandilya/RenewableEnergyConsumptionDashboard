from sqlalchemy.orm import Session
from typing import List, Optional

from schema.employee_usage_schema import EmployeeUsageCreate, EmployeeUsageUpdate, EmployeeUsageInDB
from repositories.employee_usage_db_service import *

class EmployeeUsageService:

    def __init__(self):
        self.BASE_EMISSION_PER_HOUR = 0.05  # kWh/hour for laptop usage
        self.DARK_MODE_SAVING_PERCENTAGE = 0.15

    @staticmethod
    def create_employee_usage_service(db: Session, usage: EmployeeUsageCreate) -> EmployeeUsageInDB:
        return create_employee_usage(db, usage)

    @staticmethod
    def get_employee_usage_service(db: Session, emission_id: int) -> Optional[EmployeeUsageInDB]:
        return get_employee_usage_by_id(db, emission_id)

    @staticmethod
    def get_all_employee_usages_service(db: Session, skip: int = 0, limit: int = 100) -> List[EmployeeUsageInDB]:
        return get_all_employee_usages(db, skip, limit)

    @staticmethod
    def update_employee_usage_service(db: Session, emission_id: int, usage_update: EmployeeUsageUpdate) -> Optional[EmployeeUsageInDB]:
        return update_employee_usage(db, emission_id, usage_update)

    @staticmethod
    def delete_employee_usage_service(db: Session, emission_id: int) -> bool:
        return delete_employee_usage(db, emission_id)



    def calculate_emission_saved(self, total_active_hours: int, dark_mode: float):
        base_emission = total_active_hours * self.BASE_EMISSION_PER_HOUR
        saving = base_emission * self.DARK_MODE_SAVING_PERCENTAGE * dark_mode  # Save only if dark mode enabled
        return base_emission - saving

    def log_employee_usage(self, db: Session, usage: EmployeeUsageCreate):
        return create_usage_entry(db, usage)

    def fetch_employee_usages(self, db: Session, employee_id: int):
        return get_employee_usages(db, employee_id)



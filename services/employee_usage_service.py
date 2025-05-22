from sqlalchemy.orm import Session
from typing import List, Optional

from schema.employee_usage_schema import EmployeeUsageCreate, EmployeeUsageUpdate, EmployeeUsageInDB
from repositories.employee_usage_db_service import (
    create_employee_usage,
    get_employee_usage_by_id,
    get_all_employee_usages,
    update_employee_usage,
    delete_employee_usage
)

class EmployeeUsageService:

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

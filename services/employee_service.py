from sqlalchemy.orm import Session
from typing import List, Optional

from schema.employee_schema import EmployeeCreate, EmployeeInDB
from repositories.employee_db_service import *
from utils.database import get_db

class EmployeeService:

    @staticmethod
    def create_employee_service(db: Session, employee: EmployeeCreate) -> EmployeeInDB:
        return create_employee(db, employee)

    @staticmethod
    def get_employee_service(db: Session, employee_id: int) -> Optional[EmployeeInDB]:
        return get_employee_by_id(db, employee_id)

    @staticmethod
    def get_all_employees_service(db: Session, skip: int = 0, limit: int = 100) -> List[EmployeeInDB]:
        return get_all_employees(db, skip, limit)

    @staticmethod
    def update_employee_service(db: Session, employee_id: int, employee: EmployeeCreate) -> Optional[EmployeeInDB]:
        return update_employee(db, employee_id, employee)

    @staticmethod
    def delete_employee_service(db: Session, employee_id: int) -> bool:
        return delete_employee(db, employee_id)

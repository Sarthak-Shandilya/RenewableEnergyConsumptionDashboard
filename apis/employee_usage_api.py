from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schema.employee_usage_schema import EmployeeUsageCreate, EmployeeUsageInDB
from services.employee_usage_service import EmployeeUsageService

router = APIRouter(prefix="/usages", tags=["Employee Usages"])

@router.post("/", response_model=EmployeeUsageInDB)
def create_usage(usage: EmployeeUsageCreate, db: Session = Depends(get_db)):
    return EmployeeUsageService.log_employee_usage(db, usage)

@router.get("/{employee_id}", response_model=list[EmployeeUsageInDB])
def get_usages(employee_id: int, db: Session = Depends(get_db)):
    return EmployeeUsageService.fetch_employee_usages(db, employee_id)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from utils.database import get_db
from schema.employee_schema import EmployeeCreate, EmployeeInDB
from services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/add_employee", response_model=EmployeeInDB)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeService.create_employee_service(db, employee)


@router.get("/", response_model=List[EmployeeInDB])
def get_all_employees(db: Session = Depends(get_db)):
    return EmployeeService.get_all_employees_service(db)


@router.get("/{employee_id}", response_model=EmployeeInDB)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService.get_employee_service(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeInDB)
def update_employee_by_id(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
):
    updated = EmployeeService.update_employee_service(db, employee_id, employee)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.delete("/{employee_id}", status_code=204)
def delete_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    deleted = EmployeeService.delete_employee_service(db, employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")

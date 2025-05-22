from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeUsageStatBase(BaseModel):
    employee_id: Optional[int] = None
    date: Optional[date] = None
    total_active_hours: Optional[float] = None
    darkmode_on: Optional[float] = None
    battery_usage: Optional[float] = None
    on_charge_usage: Optional[float] = None
    energy_usage: Optional[float] = None
    carbon_emission: Optional[float] = None

class EmployeeUsageStatCreate(EmployeeUsageStatBase):
    pass

class EmployeeUsageStatInDB(EmployeeUsageStatBase):
    emission_id: int

    class Config:
        orm_mode = True

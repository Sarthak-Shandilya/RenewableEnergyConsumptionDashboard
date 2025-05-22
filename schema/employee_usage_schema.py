from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeUsageBase(BaseModel):
    employee_id: Optional[int] = None
    total_active_hours: Optional[float] = None
    dark_mode: Optional[bool] = None
    battery_usage: Optional[int] = None
    on_charge_usage: Optional[float] = None
    energy_used_kwh: Optional[float] = None
    carbon_emission: Optional[float] = None

class EmployeeUsageCreate(EmployeeUsageBase):
    pass

class EmployeeUsageUpdate(EmployeeUsageBase):
    pass

class EmployeeUsageInDB(EmployeeUsageBase):
    emission_id: int

    class Config:
        from_attributes = True

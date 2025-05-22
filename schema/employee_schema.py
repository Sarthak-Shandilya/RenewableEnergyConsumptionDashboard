from pydantic import BaseModel
from typing import Optional
from schema.zone_schema import ZoneInDB

class EmployeeBase(BaseModel):
    name: Optional[str] = None
    zone_id: Optional[int] = None
    brightness_mode_laptop: Optional[bool] = None
    on_charge: Optional[bool] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeInDB(EmployeeBase):
    employee_id: int

    class Config:
        from_attributes = True
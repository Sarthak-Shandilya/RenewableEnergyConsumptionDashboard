# CREATE TABLE Employee (
#     employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     zone_id INTEGER,                  -- FK to Zone
#     brightness_mode_laptop boolean,             -- '0' or '1'
#     FOREIGN KEY (zone_id) REFERENCES Zone(zone_id)
# );

from pydantic import BaseModel
from typing import Optional
from schema.zone_schema import ZoneInDB

class EmployeeBase(BaseModel):
    name: str
    zone_id: Optional[int] = None
    brightness_mode_laptop: Optional[bool] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeInDB(EmployeeBase):
    employee_id: int

    class Config:
        orm_mode = True

# Optional: if you want an Employee response with nested Zone data
class EmployeeWithZone(EmployeeInDB):
    zone: Optional[ZoneInDB]
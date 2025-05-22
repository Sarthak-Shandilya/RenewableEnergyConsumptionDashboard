from pydantic import BaseModel
from datetime import date
from typing import Optional

class ZoneUsageBase(BaseModel):
    zone_id: Optional[int] = None
    date: Optional[date] = None
    energy_usage: Optional[float] = None
    carbon_emission: Optional[float] = None

class ZoneUsageCreate(ZoneUsageBase):
    pass

class ZoneUsageStatInDB(ZoneUsageBase):
    id: int

    class Config:
        orm_mode = True
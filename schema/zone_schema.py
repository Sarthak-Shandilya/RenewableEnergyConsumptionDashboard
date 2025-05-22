from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ZoneType(str, Enum):
    high = "high"
    moderate = "moderate"
    low = "low"

class ZoneBase(BaseModel):
    floor_number: Optional[int] = None
    max_occupancy: Optional[int] = None
    current_occupancy: Optional[int] = None
    appliance_usage_mode: Optional[bool] = None
    zone_type: Optional[ZoneType] = None
    active: Optional[bool] = None

class ZoneCreate(ZoneBase):
    pass

class ZoneUpdate(ZoneBase):
    pass

class ZoneInDB(ZoneBase):
    zone_id: int

    class Config:
        from_attributes = True

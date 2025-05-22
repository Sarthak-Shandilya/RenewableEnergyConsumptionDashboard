from pydantic import BaseModel
from typing import Optional

class ZoneBase(BaseModel):
    floor_number: Optional[int] = None
    max_occupancy: Optional[int] = None
    current_occupancy: Optional[int] = None
    applican_usage_mode: Optional[bool] = None
    energy_consumption_estimation: Optional[int] = None

class ZoneCreate(ZoneBase):
    pass

class ZoneUpdate(ZoneBase):
    pass

class ZoneInDB(ZoneBase):
    zone_id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional

class PointsBase(BaseModel):
    employee_id: Optional[int] = None
    current_points: Optional[int] = None
    total_points: Optional[int] = None
    converted_to_awe: Optional[bool] = None

class PointsCreate(PointsBase):
    pass

class PointsInDB(PointsBase):
    point_id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from enum import Enum
from typing import Optional


class ActionBase(BaseModel):
    action_name: Optional[str] = None
    reward: Optional[int] = None

class ActionCreate(ActionBase):
    pass

class ActionInDB(ActionBase):
    action_id: int

    class Config:
        from_attributes = True

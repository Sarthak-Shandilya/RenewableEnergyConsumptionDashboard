from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from utils.database import Base
import enum

class ZoneType(enum.Enum):
    high = "high"
    moderate = "moderate"
    low = "low"


class Zone(Base):
    __tablename__ = "zone"

    zone_id = Column(Integer, primary_key=True, autoincrement=True)
    floor_number = Column(Integer)
    max_occupancy = Column(Integer)
    current_occupancy = Column(Integer)
    appliance_usage_mode = Column(Boolean)
    zone_type = Column(Enum(ZoneType))
    active = Column(Boolean)

    # Optional: Reverse relation for Employees in this Zone
    employees = relationship("Employee", back_populates="zone")
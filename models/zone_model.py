from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.base import Base

class Zone(Base):
    __tablename__ = "zone"

    zone_id = Column(Integer, primary_key=True, autoincrement=True)
    floor_number = Column(Integer)
    max_occupancy = Column(Integer)
    current_occupancy = Column(Integer)
    applican_usage_mode = Column(Boolean)
    energy_consumption_estimation = Column(Integer)

    # Optional: Reverse relation for Employees in this Zone
    employees = relationship("Employee", back_populates="zone")
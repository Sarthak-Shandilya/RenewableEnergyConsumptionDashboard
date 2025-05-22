from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.base import Base


class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    zone_id = Column(Integer, ForeignKey("zone.zone_id"), nullable=True)
    brightness_mode_laptop = Column(Boolean, nullable=True)
    on_charge = Column(Boolean, nullable=True)
    zone = relationship("Zone")

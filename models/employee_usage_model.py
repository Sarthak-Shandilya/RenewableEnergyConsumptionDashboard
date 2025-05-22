from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from utils.database import Base

class EmployeeUsage(Base):
    __tablename__ = "employee_usage"

    emission_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.employee_id"))
    date = Column(Date, nullable=False)
    total_active_hours = Column(Integer)
    battery_usage = Column(Integer)
    dark_mode = Column(Float)
    energy_used_kwh = Column(Float)
    emission_saved = Column(Float)

    employee = relationship("Employee")
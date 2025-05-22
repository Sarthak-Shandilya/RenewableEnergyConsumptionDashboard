from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.base import Base

class Points(Base):
    __tablename__ = "points"

    point_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employee.employee_id"))
    current_points = Column(Integer)
    total_points = Column(Integer)
    converted_to_awe = Column(Integer)

    employee = relationship("Employee")
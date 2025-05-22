from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from utils.database import Base
import enum


class Action(Base):
    __tablename__ = "actions"

    action_id = Column(Integer, primary_key=True, autoincrement=True)
    action_type = Column(String)
    reward = Column(String)

    points = relationship("Points")
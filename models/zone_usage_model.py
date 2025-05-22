from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from utils.base import Base

class ZoneUsage(Base):
    __tablename__ = "zone_usage"

    zone_emission_id = Column(Integer, primary_key=True, autoincrement=True)
    zone_id = Column(Integer, ForeignKey("zone.zone_id"))
    date = Column(Date, nullable=False)
    energy_usage = Column(Float)
    carbon_emission = Column(Float)
    zone = relationship("Zone")
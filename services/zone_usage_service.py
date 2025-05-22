from sqlalchemy.orm import Session
from models.zone_usage import ZoneUsage


class ZoneUsageService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_zone_usage(self, zone_id: int, date, energy_usage: float, carbon_emission: float) -> ZoneUsage:
        zone_usage = ZoneUsage(
            zone_id=zone_id,
            date=date,
            energy_usage=energy_usage,
            carbon_emission=carbon_emission
        )
        self.db.add(zone_usage)
        self.db.commit()
        self.db.refresh(zone_usage)
        return zone_usage

    def delete_zone_usage(self, zone_emission_id: int) -> bool:
        usage = self.db.query(ZoneUsage).filter(ZoneUsage.zone_emission_id == zone_emission_id).first()
        if usage:
            self.db.delete(usage)
            self.db.commit()
            return True
        return False

    def update_zone_usage(self, zone_emission_id: int, **kwargs) -> ZoneUsage | None:
        usage = self.db.query(ZoneUsage).filter(ZoneUsage.zone_emission_id == zone_emission_id).first()
        if not usage:
            return None

        for key, value in kwargs.items():
            if hasattr(usage, key):
                setattr(usage, key, value)

        self.db.commit()
        self.db.refresh(usage)
        return usage

    def get_all_zone_usages(self) -> list[ZoneUsage]:
        return self.db.query(ZoneUsage).all()

    def get_zone_usage_by_id(self, zone_emission_id: int) -> ZoneUsage | None:
        return self.db.query(ZoneUsage).filter(ZoneUsage.zone_emission_id == zone_emission_id).first()

    

#########################
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.zone_usage_service import ZoneUsageService
import datetime

engine = create_engine('sqlite:///example.db')  # Replace with your actual DB URL
Session = sessionmaker(bind=engine)
session = Session()

zone_usage_service = ZoneUsageService(session)

# Add
usage = zone_usage_service.add_zone_usage(
    zone_id=1,
    date=datetime.date.today(),
    energy_usage=100.5,
    carbon_emission=30.2
)

# Get all
all_usages = zone_usage_service.get_all_zone_usages()

# Get one
usage_record = zone_usage_service.get_zone_usage_by_id(usage.zone_emission_id)

# Update
updated = zone_usage_service.update_zone_usage(usage.zone_emission_id, energy_usage=120.0)

# Delete
deleted = zone_usage_service.delete_zone_usage(usage.zone_emission_id)

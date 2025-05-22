from sqlalchemy.orm import Session
from models.zone_usage_model import ZoneUsage


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


from sqlalchemy.orm import Session
from models.zone_model import Zone, ZoneType  # Assuming your Zone model is in models/zone.py


class ZoneService:
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_zone(self, floor_number: int, max_occupancy: int, current_occupancy: int, 
                 appliance_usage_mode: bool, zone_type: ZoneType) -> Zone:
        new_zone = Zone(
            floor_number=floor_number,
            max_occupancy=max_occupancy,
            current_occupancy=current_occupancy,
            appliance_usage_mode=appliance_usage_mode,
            zone_type=zone_type
        )
        self.db.add(new_zone)
        self.db.commit()
        self.db.refresh(new_zone)
        return new_zone

    def delete_zone(self, zone_id: int) -> bool:
        zone = self.db.query(Zone).filter(Zone.zone_id == zone_id).first()
        if zone:
            self.db.delete(zone)
            self.db.commit()
            return True
        return False

    def update_zone(self, zone_id: int, **kwargs) -> Zone | None:
        zone = self.db.query(Zone).filter(Zone.zone_id == zone_id).first()
        if not zone:
            return None

        for key, value in kwargs.items():
            if hasattr(zone, key):
                setattr(zone, key, value)

        self.db.commit()
        self.db.refresh(zone)
        return zone


    def get_zone_by_id(self, zone_id: int) -> Zone | None:
        return self.db.query(Zone).filter(Zone.zone_id == zone_id).first()

    def get_all_zones(self) -> list[Zone]:
        return self.db.query(Zone).all()
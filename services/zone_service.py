from sqlalchemy.orm import Session
from models.zone import Zone, ZoneType  # Assuming your Zone model is in models/zone.py


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


##############################################
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.zone import ZoneType
from services.zone_service import ZoneService

# Setup DB session
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

zone_service = ZoneService(session)

# Add a new zone
zone = zone_service.add_zone(
    floor_number=2,
    max_occupancy=50,
    current_occupancy=10,
    appliance_usage_mode=True,
    zone_type=ZoneType.moderate
)

# Update a zone
updated_zone = zone_service.update_zone(zone.zone_id, current_occupancy=20)

# Delete a zone
zone_deleted = zone_service.delete_zone(zone.zone_id)



# Get a specific zone
zone = zone_service.get_zone_by_id(1)
if zone:
    print(f"Zone ID: {zone.zone_id}, Floor: {zone.floor_number}")
else:
    print("Zone not found.")

# Get all zones
all_zones = zone_service.get_all_zones()
for z in all_zones:
    print(f"Zone ID: {z.zone_id}, Floor: {z.floor_number}")

# services/zone_service.py
from sqlalchemy.orm import Session
from typing import List, Optional

from schema.zone_schema import ZoneCreate, ZoneInDB
from repositories.zone_db_service import (
    create_zone,
    get_zone_by_id,
    get_all_zones,
    update_zone,
    delete_zone,
)

class ZoneService:

    @staticmethod
    def create_zone_service(db: Session, zone: ZoneCreate) -> ZoneInDB:
        return create_zone(db, zone)

    @staticmethod
    def get_zone_service(db: Session, zone_id: int) -> Optional[ZoneInDB]:
        return get_zone_by_id(db, zone_id)

    @staticmethod
    def get_all_zones_service(db: Session, skip: int = 0, limit: int = 100) -> List[ZoneInDB]:
        return get_all_zones(db, skip, limit)

    @staticmethod
    def update_zone_service(db: Session, zone_id: int, zone: ZoneCreate) -> Optional[ZoneInDB]:
        return update_zone(db, zone_id, zone)

    @staticmethod
    def delete_zone_service(db: Session, zone_id: int) -> bool:
        return delete_zone(db, zone_id)

# repositories/zone_db_service.py
from sqlalchemy.orm import Session
from typing import List, Optional

from models.zone_model import Zone
from schema.zone_schema import *

def create_zone(db: Session, zone: ZoneCreate) -> Zone:
    db_zone = Zone(**zone.dict())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

def get_zone_by_id(db: Session, zone_id: int) -> Optional[Zone]:
    return db.query(Zone).filter(Zone.zone_id == zone_id).first()

def get_all_zones(db: Session, skip: int = 0, limit: int = 100) -> List[Zone]:
    return db.query(Zone).offset(skip).limit(limit).all()

def update_zone(db: Session, zone_id: int, zone: ZoneCreate | ZoneUpdate) -> Optional[Zone]:
    db_zone = db.query(Zone).filter(Zone.zone_id == zone_id).first()
    if not db_zone:
        return None
    for key, value in zone.model_dump(exclude_unset=True).items():
        setattr(db_zone, key, value)
    db.commit()
    db.refresh(db_zone)
    return db_zone

def delete_zone(db: Session, zone_id: int) -> bool:
    db_zone = db.query(Zone).filter(Zone.zone_id == zone_id).first()
    if not db_zone:
        return False
    db.delete(db_zone)
    db.commit()
    return True

def get_active_employees_by_zone(db: Session, zone_id: int) -> List[int]:
    return db.query(Zone.zone_id).filter(
        Zone.zone_id == zone_id,
        Zone.active == True
    ).all()

def deactivate_zone_if_empty(db: Session, zone_id: int):
    active_employees = get_active_employees_by_zone(db, zone_id)
    if not active_employees:
        # Additional appliance shutdown logic if needed
        return True
    return False

# apis/zone_apis.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from repositories.zone_usae_db_service import analyze_zone_proximity_and_optimize
from utils.database import get_db
from schema.zone_schema import ZoneCreate, ZoneInDB
from services.zone_service import ZoneService

router = APIRouter(prefix="/zones", tags=["Zones"])

@router.post("/", response_model=ZoneInDB)
def create_zone(zone: ZoneCreate, db: Session = Depends(get_db)):
    return ZoneService.create_zone_service(db, zone)

@router.get("/", response_model=List[ZoneInDB])
def get_all_zones(db: Session = Depends(get_db)):
    return ZoneService.get_all_zones_service(db)

@router.get("/{zone_id}", response_model=ZoneInDB)
def get_zone_by_id(zone_id: int, db: Session = Depends(get_db)):
    zone = ZoneService.get_zone_service(db, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone

@router.put("/{zone_id}", response_model=ZoneInDB)
def update_zone_by_id(zone_id: int, zone: ZoneCreate, db: Session = Depends(get_db)):
    updated_zone = ZoneService.update_zone_service(db, zone_id, zone)
    if not updated_zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return updated_zone

@router.delete("/{zone_id}", status_code=204)
def delete_zone_by_id(zone_id: int, db: Session = Depends(get_db)):
    deleted = ZoneService.delete_zone_service(db, zone_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Zone not found")

@router.post("/optimize_zones")
def optimize_zones(db: Session = Depends(get_db)):
    analysis = analyze_zone_proximity_and_optimize(db)
    return {"message": "Zone occupancy and appliance optimization done.", "analysis": f"{analysis}"}

@router.get("/underutilized-zones")
def get_suggested_relocation_zones(db: Session = Depends(get_db)):
    zones = get_all_zones(db)
    suggestions = [
        {"zone_id": zone.zone_id, "occupancy": zone.current_occupancy}
        for zone in zones if zone.current_occupancy and zone.current_occupancy < (zone.max_occupancy or 4)
    ]
    return suggestions
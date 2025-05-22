from sqlalchemy.orm import Session
from repositories.zone_db_service import get_all_zones, update_zone
from repositories.zone_db_service import *
from schema.zone_schema import ZoneUpdate
from typing import List
import json
PROXIMITY_THRESHOLD = 2  # Max distance in meters for grouping

def analyze_zone_proximity_and_optimize(db: Session):
    zones = get_all_zones(db)
    if not zones:
        return json.dumps(f"No zones found")
    for zone in zones:
        active_employees = get_active_employees_by_zone(db, zone.zone_id)
        employee_count = len(active_employees)
        is_empty = deactivate_zone_if_empty(db, zone.zone_id)
        if is_empty:
            return json.dumps(f"Zone {zone.zone_id} deactivated as there are no employees.")
        updated_data = ZoneUpdate(
            current_occupancy=employee_count,
            appliance_usage_mode=(employee_count > 0)  # If no one, turn off
        )

        update_zone(db, zone.zone_id, updated_data)

        # Suggest proximity moves if needed
        if employee_count > 0 and employee_count < (zone.max_occupancy or 5):
            return json.dumps(f"Zone {zone.zone_id} underutilized. Suggest employees move closer.")
from fastapi import FastAPI
from utils.database import Base, engine
import apis.employee_apis as employee   # Import your router
import apis.zone_apis as zone
import apis.employee_usage_api as employee_usage_api
from models.employee_model import Employee
from models.zone_model import Zone
from models.points_model import Points
from models.actions_model import Action
from models.employee_usage_model import EmployeeUsage
from models.zone_usage_model import ZoneUsage

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="EcoZone Employee Tracker API",
    version="1.0.0",
)

# Include routers
app.include_router(employee.router)
app.include_router(zone.router)
app.include_router(employee_usage_api.router)
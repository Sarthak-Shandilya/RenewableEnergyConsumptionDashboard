from sqlalchemy import create_engine
<<<<<<< Updated upstream
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./RenewableEnergyHackathon.db"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()
=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./RenewableEnergyHackathon.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Only for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to use in routes and services
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
>>>>>>> Stashed changes

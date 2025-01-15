from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from databasemodels import Base
from config import config

# Use config for DB_URL
engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_db():
    """Initialize database by creating all tables"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
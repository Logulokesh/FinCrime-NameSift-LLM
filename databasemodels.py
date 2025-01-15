from sqlalchemy import Column, Integer, String, DateTime, Date, Float, ARRAY, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class WatchlistEntity(Base):
    __tablename__ = "watchlist_entities"
    id = Column(Integer, primary_key=True)
    unique_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    name_embedding = Column(Vector(1536))  # Size matches the model's output
    aliases = Column(ARRAY(String))
    dates_of_birth = Column(ARRAY(Date))
    gender = Column(String)
    nationality = Column(String)
    country_of_residence = Column(String)
    risk_category = Column(String)
    additional_info = Column(String)
    entity_type = Column(String, default="INDIVIDUAL")

class ScreeningRecord(Base):
    __tablename__ = "screening_records"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    screening_type = Column(String, nullable=False)
    screening_time = Column(DateTime, nullable=False)
    matched = Column(Boolean, default=False)
    risk_score = Column(Float)
    llm_explanation = Column(String)

class ScreeningMatch(Base):
    __tablename__ = "screening_matches"
    id = Column(Integer, primary_key=True)
    screening_id = Column(Integer, nullable=False)
    watchlist_entity_id = Column(Integer, nullable=False)
    match_type = Column(String, nullable=False)
    match_score = Column(Float, nullable=False)
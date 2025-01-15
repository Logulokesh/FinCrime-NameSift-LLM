from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import date

class DateOfBirth(BaseModel):
    year: int
    month: int
    day: int

class ScreeningRequest(BaseModel):
    name: str
    date_of_birth: Optional[Dict[str, int]] = None

class WatchlistEntity(BaseModel):
    unique_id: str
    name: str
    aliases: Optional[List[str]] = None
    dates_of_birth: Optional[List[date]] = None
    gender: Optional[str] = None
    nationality: Optional[str] = None
    country_of_residence: Optional[str] = None
    risk_category: Optional[str] = "SAN"
    additional_info: Optional[str] = None

class WatchlistUploadRequest(BaseModel):
    watchlist: List[Dict]
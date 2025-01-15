from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Request
from databaseconnection import get_db, initialize_db
from servicesscreening import ScreeningService
from sqlalchemy.orm import Session
import datetime
import logging
import csv
from io import StringIO
import json

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_event("startup")
def startup_event():
    initialize_db()

def get_screening_service(db: Session = Depends(get_db)):
    return ScreeningService(db)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float):
            if obj != obj:  # NaN
                return None
            if obj == float('inf') or obj == float('-inf'):  # inf, -inf
                return None
        return super().default(obj)

@app.post("/watchlist/upload")
async def upload_watchlist(file: UploadFile = File(None), request: Request = None, service: ScreeningService = Depends(get_screening_service)):
    try:
        watchlist = []
        if file:
            contents = await file.read()
            csv_str = contents.decode("utf-8")
            csv_file = StringIO(csv_str)
            reader = csv.DictReader(csv_file)
            for row in reader:
                row = {k: (v if v != "" else None) for k, v in row.items()}
                watchlist.append(row)
            logger.info(f"Processed CSV with {len(watchlist)} entries")
        else:
            try:
                data = await request.json()
                logger.info(f"Received JSON: {data}")
                watchlist = data.get("watchlist", [])
                if not watchlist:
                    raise HTTPException(status_code=400, detail="JSON must contain 'watchlist' key with non-empty list")
            except json.JSONDecodeError:
                raise HTTPException(status_code=400, detail="Invalid JSON format")
            except Exception as e:
                logger.error(f"JSON parsing error: {str(e)}")
                raise HTTPException(status_code=400, detail=f"JSON processing failed: {str(e)}")

        if not watchlist:
            raise HTTPException(status_code=400, detail="No valid data provided")

        processed_count = 0
        updated_count = 0
        error_count = 0
        
        for entry in watchlist:
            try:
                dob = None
                if entry.get("date_of_birth"):
                    try:
                        dob = datetime.datetime.strptime(entry["date_of_birth"], "%Y-%m-%d").date()
                        dob = [dob]
                    except ValueError:
                        logger.warning(f"Invalid date_of_birth for {entry['unique_id']}: {entry['date_of_birth']}")
                        error_count += 1
                        continue

                # Try to add or update the entity
                result = service.add_or_update_watchlist_entity(
                    unique_id=entry["unique_id"],
                    name=entry["name"],
                    dates_of_birth=dob,
                    risk_category=entry.get("risk_category")
                )
                
                if result == "created":
                    processed_count += 1
                elif result == "updated":
                    updated_count += 1
                    
            except Exception as e:
                logger.error(f"Error processing entry {entry.get('unique_id', 'unknown')}: {str(e)}")
                error_count += 1
                continue

        response_message = f"Watchlist processed successfully. Created: {processed_count}, Updated: {updated_count}"
        if error_count > 0:
            response_message += f", Errors: {error_count}"
            
        return json.loads(json.dumps({
            "created_count": processed_count,
            "updated_count": updated_count,
            "error_count": error_count,
            "message": response_message
        }, cls=CustomJSONEncoder))
        
    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Error uploading watchlist: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/screening/realtime")
async def screen_realtime(data: dict, service: ScreeningService = Depends(get_screening_service)):
    try:
        name = data.get("name")
        dob_data = data.get("date_of_birth")
        date_of_birth = None
        if dob_data:
            date_of_birth = datetime.date(
                year=dob_data["year"],
                month=dob_data["month"],
                day=dob_data["day"]
            )
        result = service.screen_entity(name=name, date_of_birth=date_of_birth)
        return json.loads(json.dumps(result, cls=CustomJSONEncoder))
    except Exception as e:
        logger.error(f"Error screening entity: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
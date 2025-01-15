from databasemodels import WatchlistEntity, ScreeningRecord, ScreeningMatch
from servicesembedding import EmbeddingGenerator
from servicesllm import LLMAnalyzer
from sqlalchemy import text
from pgvector.sqlalchemy import Vector
import datetime
import logging

logger = logging.getLogger(__name__)

class ScreeningService:
    def __init__(self, db_session):
        self.db = db_session
        self.embedding_generator = EmbeddingGenerator()
        self.llm_analyzer = LLMAnalyzer()

    def screen_entity(self, name: str, date_of_birth: datetime.date = None, screening_type: str = "Real-time"):
        try:
            name_embedding = self.embedding_generator.generate_embedding(name)
            logger.info(f"Generated embedding for name: {name}")

            screening_record = ScreeningRecord(
                name=name,
                date_of_birth=date_of_birth,
                screening_type=screening_type,
                screening_time=datetime.datetime.utcnow(),
                matched=False
            )
            self.db.add(screening_record)
            self.db.commit()
            logger.info(f"Created screening record with ID: {screening_record.id}")

            threshold = 0.6  # Changed from 0.8 to allow broader fuzzy matches
            embedding_str = f"[{','.join(map(str, name_embedding))}]"
            query = text(
                "SELECT * FROM watchlist_entities "
                "WHERE (name_embedding <=> CAST(:embedding AS vector)) < :threshold"
            )
            watchlist_entities = self.db.execute(
                query,
                {"embedding": embedding_str, "threshold": 1 - threshold}
            ).fetchall()

            logger.info(f"Found {len(watchlist_entities)} potential matches")

            matches = []
            has_matches = False

            if watchlist_entities:
                has_matches = True
                for entity in watchlist_entities:
                    match_type = "Exact" if entity.name.lower() == name.lower() else "Fuzzy"
                    match_score = 1.0 if match_type == "Exact" else 0.9

                    match_record = ScreeningMatch(
                        screening_id=screening_record.id,
                        watchlist_entity_id=entity.id,
                        match_type=match_type,
                        match_score=match_score
                    )
                    self.db.add(match_record)

                    match_details = {
                        "unique_id": entity.unique_id,
                        "name": entity.name,
                        "date_of_birth": entity.dates_of_birth[0].isoformat() if entity.dates_of_birth else None,
                        "risk_category": entity.risk_category,
                        "match_type": match_type,
                        "match_score": match_score
                    }
                    matches.append(match_details)

            screening_record.matched = has_matches
            if has_matches:
                avg_score = sum(m["match_score"] for m in matches) / len(matches)
                screening_record.risk_score = avg_score
                # Trigger LLM analysis for the first match
                screening_record.llm_explanation = self.llm_analyzer.analyze(name, matches[0])
            else:
                screening_record.llm_explanation = "No matches found"

            self.db.commit()
            logger.info("Successfully completed screening process")

            return {
                "screening_id": screening_record.id,
                "name": name,
                "date_of_birth": date_of_birth.isoformat() if date_of_birth else None,
                "screening_time": screening_record.screening_time.isoformat(),
                "matched": has_matches,
                "risk_score": screening_record.risk_score if has_matches else 0.0,
                "explanation": screening_record.llm_explanation,
                "matches": matches
            }

        except Exception as e:
            logger.error(f"Error during screening: {str(e)}")
            self.db.rollback()
            raise

    def add_watchlist_entity(self, unique_id, name, **kwargs):
        try:
            name_embedding = self.embedding_generator.generate_embedding(name)
            entity = WatchlistEntity(
                unique_id=unique_id,
                name=name,
                name_embedding=name_embedding,
                aliases=kwargs.get("aliases", []),
                dates_of_birth=kwargs.get("dates_of_birth", []),
                gender=kwargs.get("gender"),
                nationality=kwargs.get("nationality"),
                country_of_residence=kwargs.get("country_of_residence"),
                risk_category=kwargs.get("risk_category"),
                additional_info=kwargs.get("additional_info"),
                entity_type=kwargs.get("entity_type", "INDIVIDUAL")
            )
            self.db.add(entity)
            self.db.commit()
            logger.info(f"Added watchlist entity with unique_id: {unique_id}")
            return entity
        except Exception as e:
            logger.error(f"Error adding watchlist entity: {str(e)}")
            self.db.rollback()
            raise

    def add_or_update_watchlist_entity(self, unique_id, name, dates_of_birth=None, risk_category=None):
        try:
            # Convert unique_id to string to match database column type
            unique_id = str(unique_id)
            
            # Generate embedding for the name
            name_embedding = self.embedding_generator.generate_embedding(name)
            
            # Check if entity exists by unique_id
            existing_entity = self.db.query(WatchlistEntity).filter(WatchlistEntity.unique_id == unique_id).first()
            
            if existing_entity:
                # Update existing entity
                existing_entity.name = name
                existing_entity.name_embedding = name_embedding
                if dates_of_birth:
                    existing_entity.dates_of_birth = dates_of_birth
                if risk_category:
                    existing_entity.risk_category = risk_category
                self.db.commit()
                logger.info(f"Updated watchlist entity with unique_id: {unique_id}")
                return "updated"
            else:
                # Create new entity
                new_entity = WatchlistEntity(
                    unique_id=unique_id,
                    name=name,
                    name_embedding=name_embedding,
                    dates_of_birth=dates_of_birth,
                    risk_category=risk_category,
                    entity_type="INDIVIDUAL"  # Default value as per add_watchlist_entity
                )
                self.db.add(new_entity)
                self.db.commit()
                logger.info(f"Added watchlist entity with unique_id: {unique_id}")
                return "created"
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error in add_or_update_watchlist_entity for unique_id {unique_id}: {str(e)}")
            raise Exception(f"Database error: {str(e)}")
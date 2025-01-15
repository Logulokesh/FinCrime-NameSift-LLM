import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    # Database settings
    DB_USER = os.getenv("PGUSER", "lokesh")
    DB_PASSWORD = os.getenv("PGPASSWORD", "lokesh")
    DB_HOST = os.getenv("PGHOST", "localhost")
    DB_PORT = os.getenv("PGPORT", "5432")
    DB_NAME = os.getenv("PGDATABASE", "wlmscreening_db")
    DB_URL = os.getenv("DATABASE_URL", 
                      f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    # API settings
    API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
    SCREENING_API_URL = f"{API_BASE_URL}/screening/realtime"
    UPLOAD_API_URL = f"{API_BASE_URL}/watchlist/upload"

    # LLM settings
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")

    # Embedding settings
    EMBEDDING_SIZE = 1536  # Matches the vector column size in database

# Instance of Config for easy import
config = Config()
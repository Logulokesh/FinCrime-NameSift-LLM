<h1 align="center">🛡️ FinCrime NameSift LLM</h1>

<p align="center"><em>Advanced AI-Powered Financial Crime Detection & Name Screening Platform</em></p>

<p align="center">
  Transform your compliance operations with <strong>FinCrime-NameSift-LLM</strong>, the cutting-edge screening platform that combines machine learning, natural language processing, and vector-based similarity matching to identify high-risk entities in real-time. Built for financial institutions, fintech companies, and compliance teams who demand precision and speed in combating financial crime. 🎯
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Backend-FastAPI-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-informational?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Ollama-orange?style=for-the-badge" />
</p>

---

## ✨ Core Capabilities & Features

### 🔍 **Intelligent Screening Engine**
- ⚡ **Real-time Processing**: Lightning-fast customer screening with sub-second response times
- 🧠 **Fuzzy Matching**: Advanced name matching algorithms that catch variations and misspellings
- 📊 **Dynamic Risk Scoring**: AI-generated risk assessments with confidence intervals
- 🎯 **Multi-dimensional Analysis**: Cross-reference names, DOB, nationality, and aliases

### 📋 **Watchlist Management Suite**
- 📤 **Multi-format Ingestion**: Support for CSV, JSON, and ISO 20022 XML (MX) standards
- 🔄 **Bulk Processing**: Handle thousands of watchlist entries simultaneously
- 🏷️ **Smart Categorization**: Automatic classification of PEPs, sanctions, and adverse media
- 📈 **Data Validation**: Built-in checks for data integrity and completeness

### 🤖 **AI-Powered Analytics**
- 💡 **LLM Risk Explanations**: Natural language explanations for every match
- 📊 **Confidence Scoring**: Probability-based matching with tunable thresholds
- 🔮 **Predictive Insights**: Trend analysis and risk pattern recognition
- 📋 **Audit Trail**: Complete transaction history with compliance reporting

### 🎨 **Premium User Experience**
- 🌙 **Dark Mode Interface**: Modern, eye-friendly design optimized for extended use
- 📱 **Responsive Design**: Seamless experience across desktop, tablet, and mobile
- ⚡ **Progressive Loading**: Instant feedback with optimized performance
- 🎛️ **Customizable Dashboard**: Personalized widgets and reporting views

---


### 🎯 **High-Level System Overview**
```mermaid
graph TB
    A[👤 User] -->|Access| B[🖥️ Streamlit UI]
    
    B -->|Screen Customer| C[🔍 FastAPI: /screening/realtime]
    B -->|Upload Watchlist| D[📤 FastAPI: /watchlist/upload]
    B -->|View Analytics| E[📊 FastAPI: /analytics/dashboard]

    C --> F[🧠 ScreeningService]
    D --> F
    E --> F

    F -->|Generate Embedding| G[🧬 EmbeddingGenerator]
    F -->|Analyze Risk| H[⚠️ LLMAnalyzer]
    F -->|Calculate Metrics| I[📈 AnalyticsEngine]
    F -->|Store/Retrieve Data| J[🗄️ PostgreSQL + pgvector]

    J -->|Return Results| F
    F -->|Response Data| C
    C -->|Display Results| B
    D -->|Upload Status| B
    E -->|Dashboard Data| B

    %% GitHub-friendly styles for both dark & light mode
    style A fill:#1976d2,stroke:#0d47a1,stroke-width:1px
    style B fill:#7b1fa2,stroke:#4a148c,stroke-width:1px
    style C fill:#5c6bc0,stroke:#303f9f,stroke-width:1px
    style D fill:#5c6bc0,stroke:#303f9f,stroke-width:1px
    style E fill:#5c6bc0,stroke:#303f9f,stroke-width:1px
    style F fill:#f57c00,stroke:#e65100,stroke-width:1px
    style G fill:#388e3c,stroke:#1b5e20,stroke-width:1px
    style H fill:#388e3c,stroke:#1b5e20,stroke-width:1px
    style I fill:#388e3c,stroke:#1b5e20,stroke-width:1px
    style J fill:#455a64,stroke:#263238,stroke-width:1px


```

## 🏛️ System Architecture & Technology Stack

### 🎯 **Frontend Layer**
- 🌐 **Streamlit Framework**: Interactive web interface with real-time updates
- 🎨 **Custom Styling**: Branded dark theme with intuitive navigation
- 📊 **Data Visualization**: Charts, graphs, and interactive result displays
- 🔄 **State Management**: Optimized session handling and form persistence

### 🚀 **Backend Infrastructure**
- ⚡ **FastAPI Engine**: High-performance async API with automatic documentation
- 🔐 **Security Layer**: JWT authentication, rate limiting, and input validation
- 📡 **RESTful Services**: Clean API design with comprehensive error handling
- 🔄 **Load Balancing**: Horizontal scaling support for enterprise deployments

### 🧠 **AI & Machine Learning Services**
- 🤖 **Embedding Generation**: `all-MiniLM-L6-v2` transformer for semantic similarity
- 💡 **LLM Integration**: Ollama-powered risk analysis with `gemma3:12b` model
- 🔍 **Vector Search**: pgvector-optimized similarity matching
- 📊 **Model Pipeline**: Automated feature extraction and scoring algorithms

### 🗄️ **Data Management Layer**
- 🐘 **PostgreSQL Core**: ACID-compliant relational database
- 🔍 **Vector Extensions**: pgvector for high-dimensional similarity search
- 💾 **Caching Strategy**: Redis integration for performance optimization
- 🔄 **Backup & Recovery**: Automated data protection and disaster recovery

---

## 📁 Project Structure & Organization

```
🏢 fincrime-namesift-llm/
├── 📋 config/
│   ├── ⚙️ config.py              # Environment & application settings
│   ├── 🔒 security.py            # Authentication & authorization
│   └── 📊 logging.py             # Structured logging configuration
├── 🗄️ database/
│   ├── 🔌 connection.py          # Database connection management
│   ├── 📋 models.py              # SQLAlchemy ORM models
│   ├── 🔄 migrations/            # Database schema versions
│   └── 🌱 seeds/                 # Sample data for development
├── 🚀 api/
│   ├── 🌐 main.py                # FastAPI application entry point
│   ├── 📡 endpoints/             # API route definitions
│   ├── 🛡️ middleware/            # Request/response processing
│   └── ✅ validators.py          # Input validation schemas
├── 🎯 services/
│   ├── 🔍 screening.py           # Core screening business logic
│   ├── 🤖 embedding.py           # ML embedding generation
│   ├── 💡 llm.py                 # AI analysis & explanations
│   ├── 📋 watchlist.py           # Watchlist management
│   └── 📊 analytics.py           # Reporting & insights
├── 🌐 frontend/
│   ├── 🎨 ui.py                  # Streamlit application
│   ├── 📊 components/            # Reusable UI components
│   ├── 🎭 styles/                # Custom CSS & themes
│   └── 📱 pages/                 # Application screens
├── 🧪 tests/
│   ├── 🔬 unit/                  # Unit test suites
│   ├── 🔗 integration/           # Integration test cases
│   └── 🎭 e2e/                   # End-to-end scenarios
├── 📚 docs/
│   ├── 📖 api/                   # API documentation
│   ├── 👥 user/                  # User guides & tutorials
│   └── 🛠️ deployment/            # Infrastructure guides
├── 🔧 scripts/
│   ├── 🚀 deploy.sh              # Deployment automation
│   ├── 🌱 seed-data.py           # Data initialization
│   └── 🧹 cleanup.py             # Maintenance utilities
└── 📦 requirements/
    ├── 🎯 base.txt               # Core dependencies
    ├── 🧪 dev.txt                # Development tools
    └── 🚀 prod.txt               # Production requirements
```

---

## 🔄 Application Workflows & Data Flow


### 🔍 **Detailed Customer Screening Sequence**
```mermaid
sequenceDiagram
    actor User as 👤 User
    participant UI as 🖥️ Streamlit UI
    participant API as 🔌 FastAPI
    participant SS as 🧠 ScreeningService
    participant EG as 🧬 EmbeddingGenerator
    participant LLM as ⚠️ LLMAnalyzer
    participant Analytics as 📈 AnalyticsEngine
    participant DB as 🗄️ PostgreSQL

    👤 User->>🖥️ Streamlit UI: Enter customer details
    🖥️ Streamlit UI->>🔌 FastAPI: POST /screening/realtime
    🔌 FastAPI->>🧠 ScreeningService: screen_entity(name, dob, threshold)
    
    🧠 ScreeningService->>🧬 EmbeddingGenerator: generate_embedding(customer_name)
    🧬 EmbeddingGenerator-->>🧠 ScreeningService: Embedding vector (1536-dim)
    
    🧠 ScreeningService->>🗄️ PostgreSQL: Vector similarity search
    🗄️ PostgreSQL-->>🧠 ScreeningService: Potential matches with scores
    
    alt 🟢 High-confidence matches found
        🧠 ScreeningService->>⚠️ LLMAnalyzer: analyze_risk(customer, matches)
        ⚠️ LLMAnalyzer-->>🧠 ScreeningService: Risk explanation & confidence
        🧠 ScreeningService->>📈 AnalyticsEngine: update_screening_metrics()
        🧠 ScreeningService->>🗄️ PostgreSQL: Save ScreeningRecord + Matches
    else 🔵 No significant matches
        🧠 ScreeningService->>🗄️ PostgreSQL: Save ScreeningRecord (clean)
        🧠 ScreeningService->>📈 AnalyticsEngine: update_clean_screening_stats()
    end
    
    🗄️ PostgreSQL-->>🧠 ScreeningService: Persistence confirmation
    🧠 ScreeningService-->>🔌 FastAPI: Comprehensive screening results
    🔌 FastAPI-->>🖥️ Streamlit UI: JSON response with UI data
    🖥️ Streamlit UI-->>👤 User: Interactive results display

```

---

## 🛠️ Installation & Configuration Guide

### 🔧 **System Requirements**
- 🐍 **Python**: 3.8+ (recommended: 3.11+)
- 🗄️ **Database**: PostgreSQL 14+ with pgvector extension
- 💡 **AI Engine**: Ollama server with gemma3:12b model
- 💾 **Memory**: Minimum 8GB RAM (16GB+ recommended)
- 💽 **Storage**: 50GB+ free space for embeddings and logs

### 📥 **Quick Start Installation**

#### 1️⃣ **Repository Setup**
```bash
git clone https://github.com/your-org/fincrime-namesift-llm.git
cd fincrime-namesift-llm
```

#### 2️⃣ **Environment Configuration**
Create your `.env` file with these enhanced settings:

```env
# 🗄️ Database Configuration
PGUSER=screening_admin
PGPASSWORD=your_secure_password_here
PGHOST=localhost
PGPORT=5432
PGDATABASE=wlmscreening_db
DATABASE_URL=postgresql://screening_admin:your_secure_password_here@localhost:5432/wlmscreening_db

# 🚀 API Configuration
API_BASE_URL=http://localhost:8000
API_VERSION=v1
API_TITLE="FinCrime-NameSift-LLM Platform"
DEBUG_MODE=false
CORS_ORIGINS=http://localhost:8501,http://localhost:3000

# 💡 AI & ML Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma3:12b
EMBEDDING_MODEL=all-MiniLM-L6-v2
EMBEDDING_CACHE_SIZE=10000
SIMILARITY_THRESHOLD=0.85

# 🔐 Security Settings
JWT_SECRET_KEY=your_jwt_secret_key_minimum_32_characters
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
API_RATE_LIMIT=100/minute

# 📊 Analytics & Monitoring
ENABLE_ANALYTICS=true
LOG_LEVEL=INFO
METRICS_ENABLED=true
PERFORMANCE_MONITORING=true

# 🎯 Business Logic
DEFAULT_RISK_THRESHOLD=0.7
MAX_MATCHES_RETURNED=10
ENABLE_BATCH_PROCESSING=true
```

#### 3️⃣ **Dependency Installation**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core dependencies
pip install -r requirements/base.txt

# For development
pip install -r requirements/dev.txt
```

#### 4️⃣ **Database Initialization**
```sql
-- Connect to PostgreSQL as superuser
CREATE USER screening_admin WITH PASSWORD 'your_secure_password_here';
CREATE DATABASE wlmscreening_db OWNER screening_admin;

-- Connect to the new database
\c wlmscreening_db
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE wlmscreening_db TO screening_admin;
```

#### 5️⃣ **AI Model Setup**
```bash
# Install and configure Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required model
ollama pull gemma3:12b

# Start Ollama service
ollama serve
```

### 🚀 **Application Launch**

#### 🎯 **Development Environment**
```bash
# Terminal 1: Start the API server
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Launch the UI
streamlit run frontend/ui.py --server.port 8501

# Terminal 3: Start background workers (optional)
python scripts/worker.py
```

#### 🏭 **Production Deployment**
```bash
# Use Docker Compose for production
docker-compose up -d

# Or manual production setup
gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## 📚 User Guide & Best Practices

### 🔍 **Customer Screening Workflow**

#### 🎯 **Basic Screening Process**
1. 🌐 **Access Interface**: Navigate to `http://localhost:8501`
2. 📝 **Input Customer Data**:
   - ✅ **Required**: Full customer name
   - 📅 **Optional**: Date of birth (YYYY-MM-DD format)
   - 🌍 **Optional**: Nationality/citizenship
   - 🏢 **Optional**: Business/organization affiliation
3. 🎛️ **Configure Parameters**:
   - 🎯 Risk threshold (0.1 - 1.0)
   - 📊 Maximum matches to return
   - 🔍 Search sensitivity level
4. 🚀 **Execute Screening** and review results

#### 📊 **Understanding Results**
- 🔴 **High Risk (0.8-1.0)**: Immediate review required
- 🟡 **Medium Risk (0.5-0.79)**: Enhanced due diligence recommended  
- 🟢 **Low Risk (0.1-0.49)**: Standard processing approved
- ⚪ **No Risk (0.0)**: Clean - no matches found

### 📋 **Watchlist Management**

#### 📤 **Supported Upload Formats**

**📄 CSV Format Example:**
```csv
unique_id,name,date_of_birth,nationality,risk_category,aliases,source
WL001,John Smith,1980-01-15,US,PEP,"J. Smith;Johnny Smith",OFAC
WL002,Maria Garcia,1975-05-20,MX,SAN,"M. Garcia",UN_Sanctions
WL003,Ahmed Al-Rahman,1960-12-03,SA,AM,"A. Rahman;Ahmed Rahman",Media_Reports
```

**🔗 JSON Format Example:**
```json
{
  "watchlist": [
    {
      "unique_id": "WL001",
      "name": "John Smith",
      "date_of_birth": "1980-01-15",
      "nationality": "US",
      "risk_category": "PEP",
      "aliases": ["J. Smith", "Johnny Smith"],
      "source": "OFAC",
      "last_updated": "2024-01-15T10:30:00Z"
    }
  ]
}
```

**📋 XML (ISO 20022) Format Example:**
```xml
<Document xmlns="http://www.iso20022.org">
  <Prsn>
    <Id><PrvtId><Othr><Id>WL001</Id></Othr></PrvtId></Id>
    <Nm>John Smith</Nm>
    <BirthDt>1980-01-15</BirthDt>
    <CtryOfRes>US</CtryOfRes>
    <RskCtgy>PEP</RskCtgy>
    <Aliases>
      <Alias>J. Smith</Alias>
      <Alias>Johnny Smith</Alias>
    </Aliases>
  </Prsn>
</Document>
```

---

## 🌐 API Reference & Integration

### 📡 **Core Endpoints**

| 🔗 **Endpoint** | 🎯 **Method** | 📝 **Description** | 🔧 **Authentication** |
|----------------|---------------|-------------------|---------------------|
| `/screening/realtime` | 🚀 POST | Real-time customer screening | 🔐 JWT Required |
| `/screening/batch` | 📦 POST | Bulk screening operations | 🔐 JWT Required |
| `/watchlist/upload` | 📤 POST | Upload watchlist data | 🔐 JWT Required |
| `/watchlist/search` | 🔍 GET | Search watchlist entries | 🔐 JWT Required |
| `/analytics/dashboard` | 📊 GET | Screening statistics | 🔐 JWT Required |
| `/health` | ❤️ GET | System health check | 🌐 Public |

### 🔍 **Screening API Details**

#### 🚀 **Real-time Screening**
```bash
POST /api/v1/screening/realtime
Content-Type: application/json
Authorization: Bearer <jwt_token>

{
  "customer": {
    "name": "John Smith",
    "date_of_birth": {
      "year": 1980,
      "month": 1,
      "day": 15
    },
    "nationality": "US",
    "additional_info": "CEO of Tech Corp"
  },
  "options": {
    "risk_threshold": 0.7,
    "max_matches": 5,
    "include_explanation": true,
    "enable_fuzzy_matching": true
  }
}
```

#### 📊 **Response Format**
```json
{
  "screening_id": "uuid-12345",
  "timestamp": "2024-01-15T10:30:00Z",
  "customer": {
    "name": "John Smith",
    "date_of_birth": "1980-01-15"
  },
  "results": {
    "overall_risk_score": 0.85,
    "risk_level": "HIGH",
    "total_matches": 2,
    "processing_time_ms": 150,
    "matches": [
      {
        "match_id": "uuid-67890",
        "watchlist_entity": {
          "unique_id": "WL001",
          "name": "John Smith",
          "risk_category": "PEP",
          "source": "OFAC"
        },
        "similarity_score": 0.95,
        "confidence_level": "HIGH",
        "explanation": "Exact name match with date of birth confirmation",
        "risk_factors": [
          "Political exposure",
          "High-profile position",
          "Recent sanctions activity"
        ]
      }
    ]
  }
}
```



### ☁️ **Cloud Deployment Options**
- 🌊 **AWS**: ECS, RDS, ElastiCache
- ☁️ **Azure**: Container Instances, PostgreSQL, Redis Cache  
- 🌩️ **GCP**: Cloud Run, Cloud SQL, Memorystore


---

## 📊 Version History

### 🏷️ **Current Release: v2.1.0** 
*Released: January 2025*

#### ✨ **New Features**
- 🤖 Enhanced AI risk explanations with context
- 📊 Advanced analytics dashboard with trends
- 🔍 Improved fuzzy matching algorithms
- 🌐 Multi-language name processing support


---

<div align="center">

[![Contributors](https://contrib.rocks/image?repo=Logulokesh/KinAI-Ecosystem)](https://github.com/Logulokesh/KinAI-Ecosystem/graphs/contributors)

</div>

---


## 📄 License

This project is entirely free to use — a contribution to the fight against financial crime 💼, a commitment to transparency 🔍, and a step toward a safer financial system 💳.

---

<div align="center">

**Developed with dedication ⚖️ to integrity, security, and smart automation**

</div>


# NBA Cloud Analytics Platform

## 🏀 Version 1: Local FastAPI + SQLite

A beginner-friendly NBA player analytics API built with FastAPI and SQLite.
**No Azure yet** — just local development to learn the fundamentals.

---

## 🎯 What This Does

- Pulls NBA player data (currently sample data, real API integration coming soon)
- Stores it in a local SQLite database
- Exposes 5 REST API endpoints for querying players and stats
- Includes interactive API documentation at `/docs`

---

## 📦 Tech Stack (V1)

- **Language:** Python 3.9+
- **Framework:** FastAPI
- **Database:** SQLite (local `.db` file)
- **Server:** Uvicorn

### Future Upgrades

- Real NBA API integration
- Azure SQL Database
- Azure App Service deployment
- Docker containerization
- GitHub Actions CI/CD

---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/pawillis16/nba-cloud-analytics-platform.git
cd nba-cloud-analytics-platform/backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python main.py
```

You should see:
```
============================================================
🏀 NBA Analytics Platform - Version 1
============================================================

✅ Starting server on http://127.0.0.1:8000

📚 API Docs: http://127.0.0.1:8000/docs
🧪 Try this first: http://127.0.0.1:8000/health
```

---

## 🧪 Testing Endpoints

### Your First Win ✅

Visit this in your browser:
```
http://127.0.0.1:8000/health
```

**Response:**
```json
{"status": "ok"}
```

---

### All Available Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Check if API is running |
| `/` | GET | Show API info |
| `/players` | GET | Get all players |
| `/players/{id}` | GET | Get player by ID (e.g., `/players/1`) |
| `/players/top-scorers` | GET | Get top scorers (add `?limit=5` to customize) |
| `/analytics/stats` | GET | Get league-wide averages |

---

### Test Them in Your Browser

1. **All players:**  
   `http://127.0.0.1:8000/players`

2. **Top 5 scorers:**  
   `http://127.0.0.1:8000/players/top-scorers?limit=5`

3. **League stats:**  
   `http://127.0.0.1:8000/analytics/stats`

4. **Interactive docs:**  
   `http://127.0.0.1:8000/docs` (try endpoints directly here!)

---

## 📁 Project Structure

```
nba-cloud-analytics-platform/
├── backend/
│   ├── main.py           # FastAPI app & all 5 endpoints
│   ├── database.py       # SQLite setup & session management
│   ├── models.py         # Player database schema
│   ├── nba_data.py       # Sample player data (seed)
│   ├── requirements.txt  # Python dependencies
│   └── nba_players.db    # SQLite database (created on first run)
└── README.md
```

---

## 💡 How It Works

### On Startup (`main.py`)

1. FastAPI initializes
2. SQLite database tables are created (if needed)
3. Sample player data is inserted (once)
4. Server starts on `http://127.0.0.1:8000`

### When You Hit `/players`

1. FastAPI receives the request
2. `get_all_players()` function runs
3. It queries the SQLite database via SQLAlchemy
4. Returns list of players as JSON

### Database Flow

```
main.py → database.py (SQLite engine) → models.py (Player schema) 
→ nba_players.db (local file)
```

---

## 🔄 Next Steps (Roadmap)

### V1.1: Real Data
- [ ] Replace sample data with NBA Stats API
- [ ] Add player image URLs
- [ ] Create `/teams` endpoint

### V1.2: More Analytics
- [ ] Per-team averages
- [ ] Player comparison endpoint
- [ ] Performance trends

### V2: Cloud Ready
- [ ] Migrate SQLite → Azure SQL Database
- [ ] Deploy API to Azure App Service
- [ ] Add GitHub Actions workflows for CI/CD

### V3: Frontend
- [ ] Simple dashboard (React or plain HTML)
- [ ] Player search & filters
- [ ] Stats visualization

---

## 🐛 Debugging

### Database not creating?

The `nba_players.db` file should appear in `backend/` after first run.

```bash
ls -la backend/nba_players.db
```

### Port 8000 already in use?

```bash
python main.py  # Change port in main.py if needed
# Or kill the process using port 8000
```

### Import errors?

Make sure you're in the `backend/` folder:
```bash
cd backend
pip install -r requirements.txt
python main.py
```

---

## 📚 Learning Resources

- **FastAPI Docs:** https://fastapi.tiangolo.com
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org
- **Uvicorn Docs:** https://www.uvicorn.org

---

## 📝 Notes for Learning

- Each `.py` file has comments explaining what it does
- `database.py` shows how SQLite connects to FastAPI
- `models.py` defines the database table structure
- `main.py` is where the API logic lives
- Try modifying `SAMPLE_PLAYERS` in `nba_data.py` to add your own players!

---

## 🤝 Next: Use Codex as Your Coding Partner

When you're ready to:
- Add new endpoints
- Connect to real NBA API
- Fix bugs
- Optimize queries

Tell Codex your goal, review what it writes, understand it, then commit it.

---

**Build locally first. Deploy to Azure later.** ✅

Good luck! 🚀

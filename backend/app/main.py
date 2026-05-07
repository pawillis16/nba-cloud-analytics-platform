from fastapi import FastAPI


app = FastAPI(title="NBA Cloud Analytics Platform")


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Welcome to NBA Analytics API"}

@app.get("/players")
def get_players():
    return [
        {"name": "LeBron James", "team": "Los Angeles Lakers", "position": "SF"},
        {"name": "Stephen Curry", "team": "Golden State Warriors", "position": "PG"},
        {"name": "Luka Dončić", "team": "Los Angeles Lakers", "position": "PG"},
        {"name": "Giannis Antetokounmpo", "team": "Milwaukee Bucks", "position": "PF"}
    ]
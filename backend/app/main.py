from nba_api.stats.endpoints import leaguedashplayerstats



from fastapi import FastAPI


app = FastAPI(title="NBA Cloud Analytics Platform")


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Welcome to NBA Analytics API"}

@app.get("/real-players")
def real_players():
    data = leaguedashplayerstats.LeagueDashPlayerStats().get_dict()

    rows = data['resultSets'][0]['rowSet']

    players = []

    for row in rows[:10]:
        players.append({
            "player_name": row[1],
            "team": row[4],
            "games_played": row[6],
            "minutes": round(row[10], 1),
            "points_per_game": round(row[30] / row[6], 1)
        })

    return players

@app.get("/real-players/{team}")
def real_players_by_team(team: str):
    data = leaguedashplayerstats.LeagueDashPlayerStats().get_dict()

    rows = data["resultSets"][0]["rowSet"]

    players = []

    for row in rows:
        if row[4] == team.upper():
            players.append({
                "player_name": row[1],
                "team": row[4],
                "games_played": row[6],
                "minutes": round(row[10], 1),
                "points_per_game": round(row[30] / row[6], 1)
            })

    return players


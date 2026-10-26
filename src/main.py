from fastapi import fastAPI , BackgroundTasks
import uvicorn

from src import api_client , rss_scraper , matcher , discord_webhook
app = fastAPI( title = "Anime Release Tracker")

@app.get("/")

def read_root():
    return {"status": "Anime Tracker is online "}

#@app.get("trigger-tracker")
#def run_tracker():



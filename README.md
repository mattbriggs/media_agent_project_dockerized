# Daily Media Contact Agent (Docker + Railway Ready)

This bot automatically searches for new ebook review outlets, scrapes their contact info, and populates a Notion CRM.

## Features
- Daily Google Search via SerpAPI
- Scrapes emails or detects contact forms
- Adds new entries into Notion
- Designed for Railway.app cloud deployment
- Fully Dockerized and ready for Cron Job Scheduling

## Setup Locally
```bash
pip install -r requirements.txt
python daily_run.py
```

## Run Tests
```bash
pytest
```

## Docker Instructions
```bash
docker build -t media-agent .
docker run --rm media-agent
```

## Deploy to Railway
- Push code to GitHub
- Connect Railway to repo
- Use Railway Schedules to run daily with cron `0 9 * * *`

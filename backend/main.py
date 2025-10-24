# backend/main.py
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from models import (
    get_all_events, create_event, update_event, delete_event,
    register_participant, get_all_participants, get_participants_by_event
)

app = FastAPI(title="Campus Event Registration API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ADMIN_TOKEN = "admin123"

# Middleware authentikasi
def verify_token(x_token: str = Header(None)):
    if x_token != ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")

# --- EVENT ENDPOINTS ---

@app.get("/events")
def read_events():
    return get_all_events()

@app.post("/events")
def add_event(title: str, date: str, location: str, quota: int, token: str = Header(None)):
    verify_token(token)
    create_event(title, date, location, quota)
    return {"message": "Event created successfully"}

@app.put("/events/{event_id}")
def edit_event(event_id: int, title: str, date: str, location: str, quota: int, token: str = Header(None)):
    verify_token(token)
    update_event(event_id, title, date, location, quota)
    return {"message": "Event updated successfully"}

@app.delete("/events/{event_id}")
def remove_event(event_id: int, token: str = Header(None)):
    verify_token(token)
    delete_event(event_id)
    return {"message": "Event deleted successfully"}

# --- PARTICIPANT ENDPOINTS ---

@app.post("/register")
def register(name: str, email: str, event_id: int):
    register_participant(name, email, event_id)
    return {"message": "Registration successful"}

@app.get("/participants")
def participants(event_id: int | None = None):
    if event_id:
        return get_participants_by_event(event_id)
    return get_all_participants()


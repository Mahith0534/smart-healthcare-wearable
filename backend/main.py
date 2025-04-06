from fastapi import FastAPI
from .model.predictor import is_emergency
from .utils.alert import send_email_alert
from .schemas import HealthData

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase (only once)
cred = credentials.Certificate("backend/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

@app.post("/health-data")
async def receive_data(data: HealthData):
    print("Received:", data)

    # Upload to Firestore
    try:
        db.collection("vitals").add(data.dict())
        print("✅ Uploaded to Firestore")
    except Exception as e:
        print("❌ Firestore upload failed:", e)

    # Emergency Detection
    if is_emergency(data):
        send_email_alert(data)

    return {"status": "ok"}

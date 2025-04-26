# 🏥 Smart Healthcare Wearable System

A smart IoT-based healthcare monitoring system that simulates wearable devices to collect health vitals (heart rate, BP, SpO2, temperature), detects emergencies using an ML model, uploads data to Firebase Cloud, and sends automated email alerts to healthcare providers.

---

## 📦 Features

- Simulated wearable sending vitals in real time
- Emergency detection using machine learning
- FastAPI backend server
- Data upload to **Firebase Firestore**
- Automated **email alerts** for critical health conditions
- Easy-to-run modular design

---

## 🚀 Tech Stack

- 🐍 Python 3
- ⚡ FastAPI
- 🤖 Scikit-learn (ML Model)
- ☁️ Firebase Firestore (Cloud DB)
- 📧 SMTP for Email Alerts
- 💻 Uvicorn (Server)
- 🧪 Pydantic (Schema validation)

---

## 🧠 ML Model

Trained on synthetic health data to classify whether a vital reading indicates an **emergency** or **normal** condition based on:

- Heart Rate
- Blood Pressure (Systolic/Diastolic)
- SpO2 Level
- Body Temperature

Model saved as: `backend/model/emergency_model.pkl`

---

## 📁 Project Structure

```
smart-healthcare-wearable/
├── backend/
│   ├── main.py               # FastAPI server
│   ├── model/
│   │   ├── train_emergency_model.py
│   │   └── predictor.py
│   ├── utils/
│   │   └── alert.py          # Email alert logic
│   ├── schemas.py            # Pydantic models
│   └── serviceAccountKey.json 🔒 (NOT pushed to GitHub)
├── simulator/
│   └── wearable_simulator.py # Simulated vitals
├── run_all.sh                # Script to run everything
├── requirements.txt
└── README.md
```

---

## 🛠 Setup Instructions

### 1. 📅 Clone the Repo

```bash
https://github.com/Mahith0534/smart-healthcare-wearable.git
cd smart-healthcare-wearable
```

### 2. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. 🔐 Add Firebase Credentials

- Go to [Firebase Console](https://console.firebase.google.com/)
- Project Settings → Service Accounts → Generate Private Key
- Save it as: `backend/serviceAccountKey.json`

✅ Make sure `.gitignore` is ignoring this file.

### 4. 🧠 Train the ML Model

```bash
python backend/model/train_emergency_model.py
```

### 5. 🚀 Start Backend Server

```bash
uvicorn backend.main:app --reload
```

### 6. �ힺ Start the Wearable Simulator

```bash
python simulator/wearable_simulator.py
```

Or run everything with:

```bash
bash run_all.sh
```

---

## ☁️ Firebase Firestore

All health data is stored in the `vitals` collection. You can view it in your Firebase Console.

---

## 📧 Email Alerts

- Alerts are sent when vitals indicate an emergency
- SMTP settings can be configured in `backend/utils/alert.py`

---

## 📌 To-Do / Future Features

- Add real dashboard (React or Streamlit)
- SMS/WhatsApp alerts via Twilio
- Historical data trends & analytics
- Login/authentication support

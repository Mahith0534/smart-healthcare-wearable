import requests, random, time

def simulate_data():
    return {
        "heart_rate": random.randint(50, 150),
        "bp_systolic": random.randint(90, 180),
        "bp_diastolic": random.randint(60, 120),
        "spo2": random.randint(85, 100),
        "temperature": round(random.uniform(36.0, 39.5), 1)
    }

while True:
    data = simulate_data()
    print("Sending:", data)
    try:
        requests.post("http://localhost:8000/health-data", json=data)
    except Exception as e:
        print("❌ Error sending data:", e)
    time.sleep(5)

# train_emergency_model.py
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate synthetic health data
def generate_data(num_samples=1000):
    data = []
    for _ in range(num_samples):
        hr = random.randint(50, 150)
        sys = random.randint(90, 180)
        dia = random.randint(60, 120)
        spo2 = random.randint(85, 100)
        temp = round(random.uniform(35.0, 40.0), 1)

        # Simple emergency logic
        emergency = int(hr > 130 or sys > 160 or dia > 100 or spo2 < 90 or temp > 38.5)
        data.append([hr, sys, dia, spo2, temp, emergency])
    return pd.DataFrame(data, columns=["heart_rate", "bp_systolic", "bp_diastolic", "spo2", "temperature", "emergency"])

# Generate and split
df = generate_data()
X = df.drop("emergency", axis=1)
y = df["emergency"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "emergency_model.pkl")
print("✅ Model trained and saved as 'emergency_model.pkl'")

import joblib
from ..schemas import HealthData

model = joblib.load("backend/model/emergency_model.pkl")

def is_emergency(data: HealthData) -> bool:
    features = [[
        data.heart_rate,
        data.bp_systolic,
        data.bp_diastolic,
        data.spo2,
        data.temperature
    ]]
    return model.predict(features)[0] == 1

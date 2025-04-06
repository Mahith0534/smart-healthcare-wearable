from pydantic import BaseModel

class HealthData(BaseModel):
    heart_rate: int
    bp_systolic: int
    bp_diastolic: int
    spo2: int
    temperature: float

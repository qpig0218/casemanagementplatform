from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Chronic Disease Management Platform")

class Patient(BaseModel):
    id: int | None = None
    name: str
    condition: str
    risk_level: str

patients: List[Patient] = []

@app.get("/patients", response_model=List[Patient])
def get_patients():
    return patients

@app.post("/patients", response_model=Patient)
def add_patient(patient: Patient):
    patient.id = len(patients) + 1
    patients.append(patient)
    return patient

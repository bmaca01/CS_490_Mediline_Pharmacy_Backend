from datetime import datetime
from typing import List
from pydantic import BaseModel

class Med(BaseModel):
    medication_id: int
    dosage: int
    instructions: str
    taken_date: datetime
    duration: int

class RxMessage(BaseModel):
    pharmacy_id: int
    doctor_id: int
    patient_id: int
    medications: List[Med]
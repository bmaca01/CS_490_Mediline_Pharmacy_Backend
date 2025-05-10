import json
from copy import deepcopy
from datetime import datetime
from sqlalchemy import select, insert, desc
from app.reflections import engine, PrescriptionTable, \
    PrescriptionMedicationTable, MedicationTable, PharmacyTable, InventoryTable, \
    NotificationTable

def add_rx(rx: dict):
    with engine.begin() as conn:
        rx_str = json.dumps(rx, default=str)
        res = conn.execute(
            insert(NotificationTable)
            .values({
                "user_id": rx.pop('pharmacy_id'),
                "notification_content": rx_str
            })
        ).inserted_primary_key
        print(res[0])
        
        return res[0]

def add_rx_old(rx: dict):
    with engine.begin() as conn:
        meds = rx.get('medications')
        conn.execute(
            insert(PrescriptionTable)
            .values({
                'patient_id': rx.get('patient_id'),
                'doctor_id': rx.get('doctor_id'),
                'pharmacy_id': rx.get('pharmacy_id'),
                'amount': 0,
                'status': 'UNPAID',
            })
        )
        
        rx_id = (rx := conn.execute(
            select(PrescriptionTable)
            .order_by(desc(PrescriptionTable.c.created_at))
        ).mappings().first())['prescription_id']

        for med in meds:
            conn.execute(
                insert(PrescriptionMedicationTable)
                .values({
                    'prescription_id': rx_id,
                    'medication_id': med['medication_id'],
                    'dosage': med['dosage'],
                    'medical_instructions': med['instructions'],
                    'taken_date': med['taken_date'],
                    'duration': med['duration']
                })
            )
        
        return rx
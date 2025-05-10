from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import Session as SessionType
from app.config import settings, DevelopmentConfig, ProductionConfig

if isinstance(settings, ProductionConfig):
    engine = create_engine(
        'mysql+pymysql://',
        creator=ProductionConfig.getconn
    )
else:
    engine = create_engine(settings.DATABASE_URL)

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)
session_factory = sessionmaker(bind=engine)
Session: SessionType = scoped_session(session_factory)

PrescriptionTable = metadata_obj.tables['prescription']
PrescriptionMedicationTable = metadata_obj.tables['prescription_medication']
MedicationTable = metadata_obj.tables['medication']
InventoryTable = metadata_obj.tables['inventory']

CountryTable = metadata_obj.tables['country']
CityTable = metadata_obj.tables['city']
AddressTable = metadata_obj.tables['address']
UserTable = metadata_obj.tables['user']
PatientTable = metadata_obj.tables['patient']
DoctorTable = metadata_obj.tables['doctor']
PharmacyTable = metadata_obj.tables['pharmacy']

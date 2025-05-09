import os
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import Session as SessionType
from dotenv import load_dotenv
load_dotenv()

#connect_args = {"check_same_thread": False}

DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT', 3306)
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_URL = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DB_URL)
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)

session_factory = sessionmaker(bind=engine)
Session: SessionType = scoped_session(session_factory)
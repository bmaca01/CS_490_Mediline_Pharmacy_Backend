from functools import lru_cache
from fastapi import FastAPI

from app.routers import register_routers
import app.config as config

@lru_cache
def get_settings():
    return config.Settings()

def create_app():
    app = FastAPI(title="Mediline Pharmacy Order Service", 
                description="Order Intake",
                version="1.0.0")
    

    register_routers(app)
    return app
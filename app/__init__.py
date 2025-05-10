import os
from fastapi import FastAPI

from app.routers import register_routers
from app.config import settings

def create_app():
    app = FastAPI(title="Mediline Pharmacy Order Service", 
                  description="Order Intake", 
                  version="1.0.0")
    

    register_routers(app)
    return app
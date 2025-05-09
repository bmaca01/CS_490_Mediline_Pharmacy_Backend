from datetime import datetime
from fastapi import APIRouter
from .pharmacy import pharmacy_router

index_router = APIRouter(tags=['health'])

@index_router.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
    

def register_routers(app):
    app.include_router(index_router)
    app.include_router(pharmacy_router)
    return
from fastapi import APIRouter

from app.struct import RxMessage
from app.services import add_rx

pharmacy_router = APIRouter(
    prefix="/pubsub",
    tags=["pharmacy"]
)

@pharmacy_router.post('/pharmacy')
async def handle_rx(msg: RxMessage):
    msg_dict = msg.model_dump()
    try:
        res = add_rx(msg_dict)
        return res
    except Exception as e:
        return {'error': str(e)}
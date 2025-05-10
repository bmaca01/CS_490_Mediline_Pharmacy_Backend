from fastapi import APIRouter, Response, status

from app.struct import RxMessage
from app.services import add_rx

pharmacy_router = APIRouter(
    prefix="/pubsub",
    tags=["pharmacy"]
)

@pharmacy_router.post('/pharmacy')
async def handle_rx(msg: RxMessage, response: Response):
    msg_dict = msg.model_dump()
    try:
        res = add_rx(msg_dict)

        response.status_code = status.HTTP_202_ACCEPTED
        return {'id': res}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'error': str(e)}
from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Bookings
from app.bookings.service import BookingService
from app.database import async_session_maker

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings():
    return await BookingService.find_all()

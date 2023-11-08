from fastapi import APIRouter

from app.bookings.schemas import SBookings
from app.bookings.service import BookingService

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings() -> list[SBookings]:
    return await BookingService.find_all()

from fastapi import APIRouter

from app.bookings.service import BookingService

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings():
    return await BookingService.find_one_or_none(price=4300)

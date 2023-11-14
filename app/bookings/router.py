from fastapi import APIRouter, Depends

from app.bookings.schemas import SBookings
from app.bookings.service import BookingService
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.service import UsersService

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):  # -> list[SBookings]:
    print(user, type(user), user.email)
    return await BookingService.find_all(user_id=user.id)

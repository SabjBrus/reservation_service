from datetime import date, datetime

from fastapi import APIRouter, Depends, status, Query
from pydantic import parse_obj_as

from app.bookings.schemas import SBookings, SBookingsInfo
from app.bookings.service import BookingService
from app.exceptions import RoomCannotBeBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_user_bookings(user: Users = Depends(get_current_user)) -> list[SBookingsInfo]:
    return await BookingService.get_user_bookings(user_id=user.id)


@router.post('')
async def add_bookings(
        room_id: int,
        date_from: date = Query(..., description=f'Например, {datetime.now().date()}'),
        date_to: date = Query(..., description=f'Например, {datetime.now().date()}'),
        user: Users = Depends(get_current_user),
):
    booking = await BookingService.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
    booking_dict = parse_obj_as(SBookings, booking).dict()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict


@router.delete('/{booking_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(
        booking_id: int,
        user: Users = Depends(get_current_user),
) -> None:
    await BookingService.delete(id=booking_id, user_id=user.id)

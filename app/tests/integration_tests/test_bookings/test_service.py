from datetime import datetime

from app.bookings.service import BookingService


async def test_add_and_get_booking():
    new_booking = await BookingService.add(
        user_id=2,
        room_id=2,
        date_from=datetime.strptime('2023-07-02', '%Y-%m-%d'),
        date_to=datetime.strptime('2023-07-22', '%Y-%m-%d'),
    )

    assert new_booking.user_id == 2
    assert new_booking.room_id == 2

    new_booking = await BookingService.find_by_id(new_booking.id)

    assert new_booking is not None


async def test_add_get_and_delete_booking():
    new_booking = await BookingService.add(
        user_id=2,
        room_id=1,
        date_from=datetime.strptime('2023-08-02', '%Y-%m-%d'),
        date_to=datetime.strptime('2023-08-22', '%Y-%m-%d'),
    )

    new_booking = await BookingService.find_by_id(new_booking.id)

    assert new_booking is not None

    await BookingService.delete(id=new_booking.id)

    new_booking = await BookingService.find_by_id(new_booking.id)

    assert new_booking is None

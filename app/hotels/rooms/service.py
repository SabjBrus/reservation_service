from datetime import date

from sqlalchemy import select, func, or_, and_

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from app.service.base import BaseService


class RoomService(BaseService):
    model = Rooms

    @classmethod
    async def get_rooms_by_hotel(
            cls,
            hotel_id: int,
            date_from: date,
            date_to: date,
    ):
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id)
                   .label('count_booked_rooms'))
            .select_from(Bookings)
            .where(
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to,
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from,
                    ),
                ),
            )
            .group_by(Bookings.room_id)
            .cte('booked_rooms')
        )

        get_rooms_left = (
            select(
                Rooms.__table__.columns,
                (Rooms.quantity - func.coalesce(booked_rooms.c.count_booked_rooms, 0))
                .label('rooms_left'),
                (Rooms.price * (date_to - date_from).days)
                .label('total_cost'),
            )
            .join(
                booked_rooms,
                booked_rooms.c.room_id == Rooms.id,
                isouter=True,
            )
            .where(
                Rooms.hotel_id == hotel_id,
            )
        )
        # print(get_rooms_left.compile(engine, compile_kwargs={'literal_binds': True}))

        async with async_session_maker() as session:
            hotel_rooms = await session.execute(get_rooms_left)
            return hotel_rooms.mappings().all()

from datetime import date

from sqlalchemy import and_, func, insert, or_, select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.exceptions import BookingNotExist
from app.hotels.rooms.models import Rooms
from app.service.base import BaseService


class BookingService(BaseService):
    model = Bookings

    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        """Добавляет бронирование"""
        """
        WITH booked_rooms AS(
            SELECT * FROM bookings WHERE room_id = 1 AND
            (date_from >= '2023-05-15' AND date_from <= '2023-06-16') OR
            (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to,
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from
                        ),
                    )
                )
            ).cte('booked_rooms')

            get_rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
                ).select_from(Rooms).join(
                    booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True,
                ).where(Rooms.id == room_id).group_by(
                    Rooms.quantity, booked_rooms.c.room_id
                )

            # print(get_rooms_left.compile(engine, compile_kwargs={'literal_binds': True}))

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price,
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()

            else:
                None

    @classmethod
    async def delete(cls, **filter_by):
        """Удаляет бронирование"""
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            result = result.scalar()
            if not result:
                raise BookingNotExist
            await session.delete(result)
            await session.commit()

    @classmethod
    async def get_user_bookings(cls, user_id: int):
        """Возвращает бронирования пользователя"""
        async with async_session_maker() as session:
            get_user_bookings = (
                select(
                    Bookings.__table__.columns,
                    Rooms.__table__.columns,
                )
                .join(
                    Rooms,
                    Bookings.room_id == Rooms.id,
                    isouter=True,
                )
                .where(
                    Bookings.user_id == user_id,
                )
            )

            user_bookings = await session.execute(get_user_bookings)
            return user_bookings.mappings().all()

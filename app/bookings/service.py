from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker


class BookingService:

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Bookings)
            bookings = await session.execute(query)
            return bookings.mappings().all()

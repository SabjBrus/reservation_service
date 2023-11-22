from datetime import date, datetime

from fastapi import Query

from app.hotels.rooms.schemas import SRooms
from app.hotels.rooms.service import RoomService
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_hotel_id(
        hotel_id: int,
        date_from: date = Query(..., description=f'Например, {datetime.now().date()}'),
        date_to: date = Query(..., description=f'Например, {datetime.now().date()}'),
) -> list[SRooms]:
    return await RoomService.get_rooms_by_hotel(hotel_id, date_from, date_to)

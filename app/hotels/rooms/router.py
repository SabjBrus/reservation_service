from datetime import date

from app.hotels.rooms.schemas import SRooms
from app.hotels.rooms.service import RoomService
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_hotel_id(
        hotel_id: int,
        date_from: date,
        date_to: date,
) -> list[SRooms]:
    return await RoomService.get_rooms_by_hotel(hotel_id, date_from, date_to)

from datetime import date

from fastapi import APIRouter

from app.hotels.schemas import SHotels
from app.hotels.service import HotelService

router = APIRouter(
    prefix='/hotels',
    tags=['Отели'],
)


@router.get('')
async def get_hotels() -> list[SHotels]:
    return await HotelService.find_all()


@router.get('/{location}')
async def get_hotels_by_location(
        location: str,
        date_from: date,
        date_to: date,
):
    return await HotelService.get_hotels(location, date_from, date_to)


@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int) -> SHotels:
    return await HotelService.find_by_id(hotel_id)

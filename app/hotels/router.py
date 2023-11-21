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
    pass

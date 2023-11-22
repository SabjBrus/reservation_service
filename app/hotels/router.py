import asyncio

from datetime import date, datetime

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

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
@cache(expire=30)
async def get_hotels_by_location(
        location: str,
        date_from: date = Query(..., description=f'Например, {datetime.now().date()}'),
        date_to: date = Query(..., description=f'Например, {datetime.now().date()}'),
) -> list[SHotels]:
    # await asyncio.sleep(3)
    hotels = HotelService.get_hotels(location, date_from, date_to)
    return await hotels


@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int) -> SHotels:
    return await HotelService.find_by_id(hotel_id)

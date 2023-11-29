from datetime import date, datetime, timedelta

from fastapi import APIRouter, Query

from app.exceptions import IncorrectDates
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
# @cache(expire=30)
async def get_hotels_by_location(
        location: str,
        date_from: date = Query(..., description=f'Например, {datetime.now().date()}'),
        date_to: date = Query(..., description=f'Например, {datetime.now().date()}'),
) -> list[SHotels]:
    # await asyncio.sleep(3)
    if (date_from >= date_to) or (date_to - date_from > timedelta(days=30)):
        raise IncorrectDates
    hotels = HotelService.get_hotels(location, date_from, date_to)
    # если cache ломает функцию, то парсим в Json (зависит от sqlachemy ответа)
    # и убираем -> list[SHotels]. Итого валидируем на один шаг раньше.
    # hotels_json = parse_obj_as(list[SHotels], hotels)
    return await hotels


@router.get('/id/{hotel_id}')
async def get_hotel_by_id(hotel_id: int) -> SHotels:
    return await HotelService.find_by_id(hotel_id)

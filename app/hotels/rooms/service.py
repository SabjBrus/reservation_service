from app.hotels.rooms.models import Rooms
from app.service.base import BaseService


class RoomService(BaseService):
    model = Rooms

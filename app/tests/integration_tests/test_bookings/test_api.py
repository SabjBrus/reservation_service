import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('room_id, date_from, date_to, booked_rooms, status_code', [
    (2, '2024-05-02', '2024-05-23', 3, 200),
    (2, '2024-05-02', '2024-05-23', 4, 200),
    (2, '2024-05-02', '2024-05-23', 5, 200),
    (2, '2024-05-02', '2024-05-23', 6, 200),
    (2, '2024-05-02', '2024-05-23', 7, 200),
    (2, '2024-05-02', '2024-05-23', 8, 200),
    (2, '2024-05-02', '2024-05-23', 9, 200),
    (2, '2024-05-02', '2024-05-23', 10, 200),
    (2, '2024-05-02', '2024-05-23', 10, 409),
    (2, '2024-05-02', '2024-05-23', 10, 409),
])
async def test_add_and_get_booking(
        room_id,
        date_from,
        date_to,
        booked_rooms,
        status_code,
        authenticated_ac: AsyncClient,
):
    response = await authenticated_ac.post('/bookings', params={
        'room_id': room_id,
        'date_from': date_from,
        'date_to': date_to,
    })

    assert response.status_code == status_code

    response = await authenticated_ac.get('/bookings')

    assert len(response.json()) == booked_rooms

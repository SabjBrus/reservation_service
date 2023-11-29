import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('location, date_from, date_to, status_code', [
    ('Алтай', '2024-05-02', '2024-05-23', 200),
    ('Сочи', '2024-05-02', '2024-05-23', 200),
    ('Алтай', '2024-05-02', '2024-04-03', 400),
    ('Алтай', '2024-05-02', '2025-05-23', 400),
])
async def test_get_hotels_by_location(
    location,
    date_from,
    date_to,
    status_code,
    ac: AsyncClient,
):
    response = await ac.get(f'/hotels/{location}', params={
        'location': location,
        'date_from': date_from,
        'date_to': date_to,
    })

    assert response.status_code == status_code

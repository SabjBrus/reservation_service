from httpx import AsyncClient


async def test_register_user(ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        'email': 'bob@dilan.com',
        'password': 'bobbob',
    })
    assert response.status_code == 200

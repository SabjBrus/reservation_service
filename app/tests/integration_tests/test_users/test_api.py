import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('email, password, status_code', [
    ('bob@gmail.com', 'bob1', 200),
    ('bob22@gmail.com', 'bob22', 200),
    ('bob@gmail.com', 'bob2', 409),
    ('123333', '12345', 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        'email': email,
        'password': password,
    })
    assert response.status_code == status_code


@pytest.mark.parametrize('email, password, status_code', [
    ('test1@test.com', 'test1', 200),
    ('test2@test.com', 'test2', 200),
    ('test2@test.com', 'wrong_pass', 401),
    ('wrong@test.com', 'test2', 401),
    ('test1test.com', 'test1', 422),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/login', json={
        'email': email,
        'password': password,
    })
    assert response.status_code == status_code

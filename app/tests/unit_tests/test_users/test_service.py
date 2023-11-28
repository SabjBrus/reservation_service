import pytest

from app.users.service import UsersService


@pytest.mark.parametrize('user_id, email, exists', [
    (1, 'test1@test.com', True),
    (2, 'test2@test.com', True),
    (3, 'wrong@email.com', False),
])
async def test_find_user_by_id(user_id, email, exists):
    user = await UsersService.find_by_id(user_id)

    if exists:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user

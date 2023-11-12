from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.users.service import UsersService

pwd_contex = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def get_password_hash(password: str) -> str:
    return pwd_contex.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_contex.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersService.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user


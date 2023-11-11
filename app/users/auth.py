from passlib.context import CryptContext

pwd_contex = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return  pwd_contex.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_contex.verify(plain_password, hashed_password)

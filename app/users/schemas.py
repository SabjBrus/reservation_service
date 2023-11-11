from pydantic import BaseModel, EmailStr


class SUSerRegister(BaseModel):
    email: EmailStr
    password: str

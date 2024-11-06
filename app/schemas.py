# Định nghĩa các Pydantic model cho request và response.
# Cung cấp cách để xác định dữ liệu mà API sẽ nhận và trả về.
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str

class ItemRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str
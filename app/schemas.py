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
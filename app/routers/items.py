#Định nghĩa các endpoint liên quan đến items trong API
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ItemCreate, ItemRead, Token
from app.dependencies import get_session
from app.crud import create_item, read_item, update_item, delete_item
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from app import auth
from sqlalchemy.future import select

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Route để đăng nhập và tạo JWT
@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = {"username": "user", "hashed_password": auth.get_password_hash("password")}
    if not auth.verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Dependency để bảo vệ các route khác
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = auth.decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

@router.post("/items/", response_model=ItemRead)
async def create_item_endpoint(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    return await create_item(session, item)

@router.get("/items/{item_id}", response_model=ItemRead)
async def read_item_endpoint(item_id: int, session: AsyncSession = Depends(get_session)):
    item = await read_item(session, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=ItemRead)
async def update_item_endpoint(item_id: int, item_data: ItemCreate, session: AsyncSession = Depends(get_session)):
    item = await update_item(session, item_id, item_data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/items/{item_id}")
async def delete_item_endpoint(item_id: int, session: AsyncSession = Depends(get_session)):
    success = await delete_item(session, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}
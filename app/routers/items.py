#Định nghĩa các endpoint liên quan đến items trong API
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import ItemCreate, ItemRead
from app.dependencies import get_session
from app.crud import create_item, read_item, update_item, delete_item

router = APIRouter()

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
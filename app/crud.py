#Chứa các hàm thực hiện thao tác CRUD
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Item
from app.schemas import ItemCreate

async def create_item(session: AsyncSession, item_data: ItemCreate) -> Item:
    new_item = Item(name=item_data.name)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item

async def read_item(session: AsyncSession, item_id: int) -> Item:
    result = await session.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()

async def update_item(session: AsyncSession, item_id: int, item_data: ItemCreate) -> Item:
    item = await read_item(session, item_id)
    if item:
        item.name = item_data.name
        await session.commit()
    return item

async def delete_item(session: AsyncSession, item_id: int) -> bool:
    item = await read_item(session, item_id)
    if item:
        await session.delete(item)
        await session.commit()
        return True
    return False
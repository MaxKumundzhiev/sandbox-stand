from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.users.scheme import (
    CreateIn,
    CreateOut,
    ReadIn,
    ReadOut,
    UpdateIn,
    UpdateOut,
    DeleteIn
)


class Service:
    def __init__(
        self, db_session: AsyncGenerator[AsyncSession, None]
    ) -> None:
        db_session = db_session
    
    async def create(request: CreateIn) -> CreateOut:
        ...
    
    async def read(request: ReadIn) -> ReadOut:
        ...
    
    async def update(request: UpdateIn) -> UpdateOut:
        ...
    
    async def delete(request: DeleteIn) -> None:
        ...

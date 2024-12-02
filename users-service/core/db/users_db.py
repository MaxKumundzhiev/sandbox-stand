from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from core.configuration import cfg


class UsersDatabase:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10
        ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url, 
            echo=echo, 
            echo_pool=echo_pool, 
            pool_size=pool_size, 
            max_overflow=max_overflow
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )
    
    async def dispose(self) -> None:
        await self.engine.dispose()
    
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


users_db_interface = UsersDatabase(
    url=str(cfg.db.url), 
    echo=cfg.db.echo, 
    echo_pool=cfg.db.echo,
    pool_size=cfg.db.pool_size,
    max_overflow=cfg.db.max_overflow
)

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Launch(BaseSettings):
    host: str = "0.0.0.0"
    port: str = "8000"


class API(BaseSettings):
    prefix: str = "/api"
    version: str = "1.0"


class UsersDatabase(BaseSettings):
    url: str = "postgresql+asyncpg://user:password@localhost:5430/users"
    echo: bool = True
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Configurations(BaseSettings):
    launch: Launch = Launch()
    api: API = API()
    users_db: UsersDatabase = UsersDatabase()


cfg = Configurations()
from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager

from api.v1.users.router import router as users
from core.users_database.session import session_manager as sm


@asynccontextmanager
async def local_lifespan(app: FastAPI):
    # startup event
    # create all usersDB tables
    from core.users_database.base_model import Base as UsersDatabaseBaseModel
    async with sm.engine.begin() as connection:
        await connection.run_sync(UsersDatabaseBaseModel.metadata.create_all)
    yield
    # shutdown event



application = FastAPI()
application.include_router(router=users, prefix="/users")


# for debug purposes
if __name__ == "__main__":
    run("server:application", reload=True)


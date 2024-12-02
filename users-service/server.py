from fastapi import FastAPI
from uvicorn import run
from contextlib import asynccontextmanager


from core.configuration import cfg
from core.users_db import users_db_interface

from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # while application start up
    yield
    # while application shutdown up
    await users_db_interface.dispose()


application = FastAPI(lifespan=lifespan)
application.include_router(router=router, prefix=f"{cfg.api.prefix}/{cfg.api.version}")


# for debug purposes
if __name__ == "__main__":
    run("server:application", reload=True)


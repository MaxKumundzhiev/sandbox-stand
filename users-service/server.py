from fastapi import FastAPI
from uvicorn import run

from core.configuration import cfg
from api import router


app = FastAPI()
app.include_router(router=router, prefix=f"{cfg.api.prefix}/{cfg.api.version}")


# for debug purposes
if __name__ == "__main__":
    run("server:app", reload=True)


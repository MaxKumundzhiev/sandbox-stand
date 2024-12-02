from fastapi import FastAPI
from uvicorn import run


from api.v1.users.router import router as users


application = FastAPI()
application.include_router(router=users)


# for debug purposes
if __name__ == "__main__":
    run("server:application", reload=True)


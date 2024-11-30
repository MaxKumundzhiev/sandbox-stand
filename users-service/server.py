from fastapi import FastAPI
from uvicorn import run


app = FastAPI()

# for debug purposes
if __name__ == "__main__":
    run("server:app", reload=True)

    
from typing import Optional
from pydantic_settings import BaseSettings


class Launch(BaseSettings):
    host: str = "0.0.0.0"
    port: str = "8000"


class API(BaseSettings):
    prefix: str = "/api"
    version: str = "1.0"


class Configurations(BaseSettings):
    launch: Launch = Launch()
    api: API = API()
    

cfg = Configurations()
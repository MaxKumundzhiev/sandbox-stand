from api.v1.users.scheme import (
    CreateIn,
    CreateOut,
    ReadIn,
    ReadOut,
    UpdateIn,
    UpdateOut,
    DeleteIn,
    DeleteOut
)


class Service:
    def __init__(self) -> None:
        pass

    async def create(request: CreateIn) -> CreateOut:
        ...
    
    async def read(request: ReadIn) -> ReadOut:
        ...
    
    async def update(request: UpdateIn) -> UpdateOut:
        ...
    
    async def delete(request: DeleteIn) -> None:
        ...

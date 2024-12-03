from fastapi import APIRouter, status

from api.v1.users.service import Service
from api.v1.users.scheme import (
    CreateIn,
    CreateOut,
    ReadIn,
    ReadOut,
    UpdateIn,
    UpdateOut,
    DeleteIn
)


router = APIRouter()


@router.post(
    path="", response_model=CreateOut, status_code=status.HTTP_201_CREATED
)
async def create(request: CreateIn):
    await Service().create(request=request)


@router.get(
    path="/{id}", response_model=ReadOut, status_code=status.HTTP_200_OK
)
async def read(id: str):
    await Service().read(request=id)


@router.put(path="/{id}", response_model=UpdateOut, status_code=status.HTTP_201_CREATED)
async def update(id: str, request: UpdateIn):
    await Service().update(request=request)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str, request: DeleteIn):
    await Service().delete(request=request)
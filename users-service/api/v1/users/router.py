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


@router.post(response_model=CreateOut, status_code=status.HTTP_201_CREATED)
async def create(request: CreateIn):
    await Service().create(request)


@router.get(response_model=ReadOut, status_code=status.HTTP_200_OK)
async def read(request: ReadIn):
    await Service().read(request)


@router.put(response_model=UpdateOut, status_code=status.HTTP_201_CREATED)
async def update(request: UpdateIn):
    await Service().update(request)


@router.delete(status_code=status.HTTP_204_NO_CONTENT)
async def delete(request: DeleteIn):
    await Service().delete(request)
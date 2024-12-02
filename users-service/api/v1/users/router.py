from fastapi import APIRouter
from api.v1.users.service import Service


router = APIRouter()


@router.post()
async def create():
    await Service().create()


@router.get()
async def read():
    await Service().read()


@router.update()
async def update():
    await Service().update()


@router.delete()
async def delete():
    await Service().delete()
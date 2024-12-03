from pydantic import BaseModel


class Base(BaseModel):
    nickname: str
    email: str


class CreateIn(Base):
    ...


class CreateOut(Base):
    id: int


class ReadIn(BaseModel):
    id: int


class ReadOut(Base):
    id: int


class UpdateIn(Base):
    ...

class UpdateOut(Base):
    id: int


class DeleteIn(BaseModel):
    id: int
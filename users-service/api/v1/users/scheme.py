from pydantic import BaseModel


class Base(BaseModel):
    nickname: str
    email: str


class CreateIn(Base):
    ...


class CreateOut(Base):
    id: str


class ReadIn(BaseModel):
    id: str


class ReadOut(Base):
    id: str


class UpdateIn(Base):
    ...

class UpdateOut(Base):
    id: str


class DeleteIn(BaseModel):
    id: str
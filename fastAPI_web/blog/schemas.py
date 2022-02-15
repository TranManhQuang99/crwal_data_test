from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class Showblog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    email: Optional[str] = None


class TimeKeeper(BaseModel):
    id: int
    name: str

from enum import Enum
from typing import Set, List, Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field


class ProgrammLanguage():
    Name: str = ""
    Librarys: Set[str] = []

    def __init__(self, name, librarys):
        self.Name = name
        self.Librarys = librarys


class Profile(str, Enum):
    Name = "user"
    Password = "123"
    Languages: Set[str] = ["English", "Russian", "German"]
    ProgrammLanguages: Set[ProgrammLanguage] = [ProgrammLanguage("Python", ["fastapi", "tkinter"])]
profile = Profile

app = FastAPI()


@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != profile.Name:
        return "Wrong name"
    elif password != profile.Password:
        return "Wrong password"
    else:
        return f"Your profile"


@app.get("/")
async def get_model(name: str | None = "", password: str | None = ""):
    if name != Profile.name:
        return "Wrong name"
    elif password != Profile.password:
        return "Wrong password"
    else:
        return "Accept"

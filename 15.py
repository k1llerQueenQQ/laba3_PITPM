from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    Name: str
    Password: str


profiles = [
    {"Name": "Jack", "Password": "123"},
    {"Name": "Egor", "Password": "123"},
]


@app.get("/items/", response_model=list[Profile])
async def read_profiles():
    return profiles
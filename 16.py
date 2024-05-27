from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    Name: str
    Password: str


profiles = [
    {"Name": "Jack", "Password": "123"},
    {"Name": "Egor", "Password": "123"},
]


@app.get("/items/", response_model=list[Profile], status_code=status.HTTP_201_CREATED)
async def read_profiles():
    return profiles
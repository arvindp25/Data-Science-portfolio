from fastapi import FastAPI
from scraping import PlayerInfo

pi = PlayerInfo()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/playerinfo/{offset}")
async def read_item(offset: int):
    return pi.get_player_info(str(offset))


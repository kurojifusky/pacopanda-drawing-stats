"""
## FastAPI Server

Copyright 2021-2025 Kerby Keith Aquino
Licensed under Apache-2.0
"""
import argparse
import uvicorn
from typing import Literal
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .logger import log

parser = argparse.ArgumentParser()
parser.add_argument("--prod",
                    action="store_true",
                    help="Runs the server in production mode, disables reload")

args = parser.parse_args()


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4000",
    "http://localhost:3000",
    "https://pds.kurojifusky.com"
]
hosts = ["localhost", "127.0.0.1", "pds.kurojifusky.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["GET", "POST", "DELETE", "PATCH"]
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=hosts
)

QueryLimit = Literal["all"] | int


@app.get("/")
async def root(request: Request):
    referer = str(request.base_url).strip("/")

    return {
        "source_code": "https://github.com/kuroji-fusky/pacopanda-drawing-stats",
        "characters_url": f"{referer}/characters",
        "character_url": referer + "/character{/characters}",
        "character_apperances_url": referer + "/character{/characters}/appearances",
        "artworks_url": f"{referer}/artworks",
        "artwork_url": referer + "/artwork{/artworks}",
    }


# Ex: /character{/paco}
@app.get("/character/{character}")
async def character(character: str):
    pass


# /character{/paco}/appearances{?limit,query,range}
@app.get("/character/{character}/appearances")
async def character(character: str, limit: int, query: str, range: str):
    pass


# /characters{?limit,query,range}
@app.get("/characters")
async def characters_list(limit: int, query: str, range: str):
    pass


# Ex: /artwork{/big-tree}
@app.get("/artwork/{artwork}")
async def artworks_list():
    pass


# /artworks{?limit,query,range}
@app.get("/artworks")
async def artworks_list(limit: int, query: str, range: str):
    pass


# /status
@app.get("/status")
async def server_status():
    pass


# /new/character{?token}
@app.post("/new/character")
async def new_character(token: str):
    pass


# /new/artwork{?token}
@app.post("/new/artwork")
async def new_character(token: str):
    pass


if __name__ == "__main__":
    APP_NAME, HOST, PORT = "main:app", "localhost", 4000

    if not args.prod:
        log("info", "Running server")
        uvicorn.run(APP_NAME, host=HOST, port=PORT, reload=True)
    else:
        log("info", "Running server in production")
        uvicorn.run(APP_NAME, host=HOST, port=PORT)

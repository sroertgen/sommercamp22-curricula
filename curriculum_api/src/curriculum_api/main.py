import logging
import os
import uvicorn
from fastapi import FastAPI, Query
from get_mappings import get_mappings

logging.basicConfig(level=logging.DEBUG)

ROOT_PATH = os.getenv("ROOT_PATH", "")

def api() -> FastAPI:
    _api = FastAPI(
        root_path=ROOT_PATH,
        title="MetaQS API",
        version="0.0.1"
    )
    logging.debug(f"Launching FastAPI on root path {ROOT_PATH}")

    return _api

app = api()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/mappings")
def mappings(q: list[str] | None = Query(default=None), title="IDs of curricula objects"):
    if q:
        res = get_mappings(q)
    else:
        res = q
    return res


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

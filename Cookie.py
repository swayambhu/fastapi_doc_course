from fastapi import FastAPI, Cookie
from typing import Annotated, Union

app = FastAPI()

@app.get('/read_items/')
async def read_items(ads_id:  Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id" : ads_id}
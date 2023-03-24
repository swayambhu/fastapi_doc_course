from fastapi import FastAPI, Header
from typing import Annotated, Union, List

app = FastAPI()

# @app.get('/items/')
# async def get_items(user_agent: Annotated[Union[str, None], Header()] = None):
#     return {"User-Agent": user_agent}

@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}
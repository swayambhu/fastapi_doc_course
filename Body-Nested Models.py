from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, HttpUrl
from typing import Union

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []
    unique_tags: set[str] = ()
    image: Union[list[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]
    

     
   
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer



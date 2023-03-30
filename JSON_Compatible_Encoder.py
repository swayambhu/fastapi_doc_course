from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from typing import Union
from pydantic import BaseModel

app = FastAPI()

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None
    
@app.put("/items/{id}")
def update_item(id: str, item: Item):
    print(item)
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(json_compatible_item_data)
from typing import Union
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.requests import Request
app = FastAPI()

class DataNotFoundException(Exception):
    def __init__(self, data):
        self.data = data

@app.exception_handler(DataNotFoundException)
async def data_not_found_exception_handler(request: Request, exc: DataNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": f"Oops! the data '{exc.data}' not found."}
    )

class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str) -> Item:
    if item_id not in items:
        raise DataNotFoundException(data=item_id)
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item) -> Item:
    if item_id not in items:
        raise DataNotFoundException(data=item_id)
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app.patch("/items/{item_id}", response_model=Item)
async def partial_update_item(item_id: str, item: Item) -> Item:
    if item_id not in items:
        raise DataNotFoundException(data=item_id)
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item


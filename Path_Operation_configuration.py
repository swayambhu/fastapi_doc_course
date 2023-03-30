from typing import Union
from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()
    
class Tags(Enum):
    items = "items"
    users = "users"
    
@app.post(
    "/items/", 
    response_model=Item, 
    status_code=status.HTTP_201_CREATED, 
    tags=[Tags.items],
    response_description="The created item"
)
async def create_item(item: Item) -> Item:
    """Create an item with all the information:

    Args:
        item (Item): 
        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tax**: if the item doesn't have tax, you can omit this
        - **tags**: a set of unique tag strings for this item

    Returns:
        json: return pydantic model Item
    """
    return item

@app.get('/items/', tags=[Tags.items])
async def read_items():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=[Tags.users])
async def read_users():
    return [{"username": "johndoe"}]

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "foo"}]
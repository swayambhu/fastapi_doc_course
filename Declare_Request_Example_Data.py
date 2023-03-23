from pydantic import BaseModel, Field
from typing import Union, Annotated
from fastapi import FastAPI, Body

app = FastAPI()

class Item(BaseModel):
    name: str = Field(example="foo")
    description: Union[str, None] = Field(None, example="A very nice item")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(None, example=3.2)
    
    # class Config:
    #     schema_extra = {
    #         "example":
    #             {
    #                 "name": "foo",
    #                 "description": "A very nice item",
    #                 "price": 35.4,
    #                 "tax": 3.2
    #             }
    #     }
        
        
# @app.put("items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.put("items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(
#     example={
#         "name": "foo",
#         "description": "A very nice item",
#         "price": 35.4,
#         "tax": 3.2
#     }
# )]):
#     results = {"item_id": item_id, "item": item}
#     return results

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

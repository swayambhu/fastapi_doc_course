from typing import Union, List
from typing_extensions import Annotated
from fastapi import FastAPI, Query
from pydantic import Required
app = FastAPI()

#? Optional Value
# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50, regex="^fixedquery$")] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q: 
#         results.update({"q": q})
#     return results

#? Required Value
# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3)]):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q: 
#         results.update({"q": q})
#     return results

#? Required Value with Ellipsis
# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q: 
#         results.update({"q": q})
#     return results

#? Required Value with Required
# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = Required):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#? Query parameter list / Multiple values
@app.get("/items/")
async def read_items(q: Annotated[Union[list, None],Query()]):
    query_items = {"q": q}
    return query_items
    
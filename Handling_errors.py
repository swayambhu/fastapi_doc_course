from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

# !HTTPException 
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="item not found")
#     return {"item": items.get(item_id)}
    

#! Add headers to HTTP Exception
# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="item not found", headers={"X-Error": "There goes my error"})
#     return {"item": items.get(item_id)}


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name
        

#! Custom Exception Handlers
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow"}
    )
    
@app.get("/unicorn/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


#!Over ride the HTTPException

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope I don't like 3.")
#     return {"item_id": item_id}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
    )

class Item(BaseModel):
    title: str
    size: int
    
@app.post("/items/")
async def create_item(item: Item):
    return item
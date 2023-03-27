from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Union, Any

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: list[str] = []
    
    
# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Item:
#     return item

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None
    
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None
    
class UserIn(BaseUser):
    password: str
    
@app.post("/user/", response_model=BaseUser)
async def create_user(user: UserIn) -> BaseUser:
    return user


@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

# @app.post("/user/", response_model=UserIn, response_model_exclude={"password"})
# async def create_user(user: UserIn) -> UserIn:
#     return user
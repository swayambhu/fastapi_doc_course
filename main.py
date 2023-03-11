from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from enum import Enum
from typing import Union

app = FastAPI()

class Name(Enum):
    swayabhu = "Swayambhu"
    Omkar = "Omkar"
    Aditya = "Aditya"

class BloodGroup(Enum):
    A_Positive = "A+"
    A_Negative = "A-"
    B_Positive = "B+"
    B_Negative = "B-"
    
    
class UserData(BaseModel):
    name: str
    email: str
    phone_no: int
    blood_group: BloodGroup
    profile_image: str = "my_profile_image.png"
    
    
@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/items/{items_id}")
async def get_item(items_id: int):
    return {"item_id": items_id}

@app.get("/model/{model_name}")
async def get_person(model_name: Name):
    return {"model_name": model_name}

@app.get("/files/{files_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

dummy_data = ['new', 'data', 'in', 'play', 'with', 'fastapi']

@app.get("/data/")
async def get_data(skip: int = 0, limit: int = 10):
    return {"dummy_data": dummy_data[skip: skip + limit]}

@app.put("/user_data/")
async def get_user_data(data: UserData):
    return {"user_data": data}

@app.get('/query_parameters/')
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get('/numbers/{q}')
async def get_numbers(q: int = Path(gt=0, lt=100)):
    return q 
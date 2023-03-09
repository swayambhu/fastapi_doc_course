from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Name(Enum):
    swayabhu = "Swayambhu"
    Omkar = "Omkar"
    Aditya = "Aditya"
    
    
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
from fastapi import FastAPI;

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/items/{items_id}")
async def get_item(items_id: int):
    return {"item_id": items_id}
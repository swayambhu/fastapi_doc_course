from fastapi import FastAPI, Depends

from typing import Union, Annotated

app = FastAPI()

async def common_parameters(
    q: Union[str, None] = None,
    skip: int = 0,
    limit: int = 100
):
    return {
        "q": q,
        "skip": skip,
        "limit": limit
    }
    

# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons

# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons

CommonDependencies = Annotated[dict, Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons: CommonDependencies):
    return commons

@app.get("/users/")
async def read_users(commons: CommonDependencies):
    return commons
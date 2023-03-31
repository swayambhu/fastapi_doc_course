from typing import Annotated, Union
from fastapi import Depends, FastAPI

app = FastAPI()

async def common_parameter(
    q: Union[str, None] = None, skip: int = 0, limit: int = 10
):
    return {
        "q": q,
        "skip": skip,
        "limit": limit
    }
    
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameter)]):

    return commons

class Cat:
    def __init__(self, name: str):
        self.name = name



fluffy = Cat(name="Mr Fluffy")

fake_users_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParameters:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
        

# CommonQueryParamDependencies = Annotated[CommonQueryParameters, Depends(CommonQueryParameters)]
CommonQueryParamDependencies = Annotated[CommonQueryParameters, Depends()]


@app.get("/users/")
async def read_users(commons: CommonQueryParamDependencies):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    users = fake_users_db[commons.skip: commons.skip + commons.limit]
    print(users)
    response.update({"users": users})
    return response

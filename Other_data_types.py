from fastapi import Body, FastAPI
from datetime import datetime, time, timedelta
from typing import Annotated, Union
from uuid import UUID

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[Union[datetime, None], Body()] = None,
    end_datetime: Annotated[Union[datetime, None], Body()] = None,
    repeat_at: Annotated[Union[time, None], Body()] = None,
    process_after: Annotated[Union[timedelta, None], Body()] = None
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return{
        "item_id": item_id,
        "start_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }
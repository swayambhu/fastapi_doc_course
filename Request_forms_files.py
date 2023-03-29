from fastapi import FastAPI, File, UploadFile, Form
from typing import Annotated

app = FastAPI()

@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()], 
    file_b: Annotated[UploadFile, File()], 
    token: Annotated[str, Form()]):
    return{
        "file_size": len(file),
        "token": token,
        "file_b_content_type": file_b.content_type  
    }
    
    

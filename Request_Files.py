from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing_extensions import Annotated

app = FastAPI()

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


# @app.post("/upload-file/")
# async def create_upload_file(file : UploadFile):
#     contents = file.file.read()
#     print(contents)
#     return {"filename": file.filename}

# @app.post("/files/")
# async def create_file(file: Annotated[Union[bytes, None], File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}
    
# @app.post("/upload-file/")
# async def create_file(file: Union[UploadFile, None] = None):
#     if not file: 
#         return {"message": "No Upload file sent"}
#     else:
#         return {"filename": file.filename}
    
# @app.post("/files/")
# async def create_upload_file(file: Annotated[bytes, File(description="A file read as Upload byte")]):
#     return {"file_size": len(file)}

# @app.post("/upload-file/")
# async def create_upload_file(file: Annotated[UploadFile, File(description="A file read as Upload file")]):
#     return {"filename": file.filename}



@app.post("/files/")
async def create_files(files: Annotated[List[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/upload-files/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/upload-files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
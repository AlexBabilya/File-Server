from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

UPLOAD_DIRECTORY = "./"


class File(BaseModel):
    data: str
    name: str


@app.post("/file/")
async def create_upload_file(attachment: File):
    filename = f"{UPLOAD_DIRECTORY}/{attachment.name}"
    with open(filename, "w") as file:
        file.write(attachment.data)

    return {"message": "Message Received and Saved Successfully",
            "filename": attachment.name}


@app.post("/")
async def echo_data(data: dict):
    return data

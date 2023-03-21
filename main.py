from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    title: str
    body: str


@app.post("/message")
async def send_message(message: Message):
    return {"title": message.title, "body": message.body, "status": "delivered"}

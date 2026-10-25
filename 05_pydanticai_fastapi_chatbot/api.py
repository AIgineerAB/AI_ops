from fastapi import FastAPI
from chat_agent import chat
from data_models import ChatResponse, ChatRequest

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def joke_chat(request: ChatRequest):

    chat_response = await chat(request)

    return chat_response



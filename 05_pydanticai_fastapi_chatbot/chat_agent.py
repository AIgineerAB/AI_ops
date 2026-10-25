from pydantic_ai import Agent
from dotenv import load_dotenv
from constants import MODEL_SMALL
from data_models import ChatRequest, ChatResponse

load_dotenv()

chat_agent = Agent(
    MODEL_SMALL,
    system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add emojis in your language",
)


async def chat(request: ChatRequest):
    result = await chat_agent.run(
        request.question, message_history=request.message_history
    )

    return ChatResponse(
        response=result.output,
        message_history=result.all_messages()
    )

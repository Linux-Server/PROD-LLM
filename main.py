from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
llm = ChatOpenAI(model="gpt-5-nano")


app = FastAPI()


class ChatIn(BaseModel):
    messages: str


async def call_llm(messages: str):
    return await llm.ainvoke(messages)


async def stream_llm(messages: str):
    async for chunk in llm.astream(messages):
        if chunk.content:
            yield chunk.content


@app.post("/")
async def root(payload: ChatIn):
    res = await call_llm(payload.messages)
    return {"message": res.content}


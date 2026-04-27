from fastapi import FastAPI
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


@app.post("/")
async def root(payload: ChatIn):
    res = await call_llm(payload.messages)
    return {"message": res.content}
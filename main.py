import asyncio
import hashlib

from fastapi import FastAPI

app = FastAPI()


@app.get("/work")
async def work(io_ms: int = 50, cpu_iters: int = 20_000):
    await asyncio.sleep(io_ms / 1000)

    h = b"seed"
    for _ in range(cpu_iters):
        h = hashlib.sha256(h).digest()

    return {"io_ms": io_ms, "cpu_iters": cpu_iters, "hash": h.hex()[:16]}

from typing import Union
from contextlib import asynccontextmanager
from math import ceil

from decouple import config
from fastapi import FastAPI, HTTPException, Depends, Request, Response
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from pydantic import BaseModel
import redis.asyncio as redis

import helpers


REDIS_URL = config("REDIS_URL")


async def rate_limit_exceeded_handler(request: Request, response: Response, pexpire: int):
    expire = ceil(pexpire / 1000)
    raise HTTPException(
        status_code=429,
        detail="Too Many Requests :(",
        headers={"Retry-After": str(expire)}
    )

async def rate_limit_identifier(request: Request):
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0]
    return request.client.host + ":" + request.scope["path"]


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis_conn = redis.from_url(REDIS_URL)
    await FastAPILimiter.init(
        redis_conn,
        identifier=rate_limit_identifier,
        http_callback=rate_limit_exceeded_handler
    )
    yield
    await FastAPILimiter.close()

app = FastAPI(lifespan=lifespan)


@app.get("/", dependencies=[Depends(RateLimiter(times=2, seconds=10))])
def read_root():
    return {"Hello": "World"}


class ImageGenertionRequest(BaseModel):
    prompt: str



@app.post("/generate", dependencies=[Depends(RateLimiter(times=2, seconds=10))])
def create_image(data: ImageGenertionRequest):
    try: 
        pred_result = helpers.generate_image(data.prompt)
        return pred_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
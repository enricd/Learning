from typing import Union

from decouple import config
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import helpers


REDIS_URL = config("REDIS_URL")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class ImageGenertionRequest(BaseModel):
    prompt: str



@app.post("/generate")
def create_image(data: ImageGenertionRequest):
    try: 
        pred_result = helpers.generate_image(data.prompt)
        return pred_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
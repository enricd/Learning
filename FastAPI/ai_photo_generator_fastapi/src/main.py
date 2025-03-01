from decouple import config
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_limiter.depends import RateLimiter
from pydantic import BaseModel

import helpers
from helpers.rate_limiting import lifespan as rate_limiter_lifespan


API_KEY_HEADER = "X-API-Key"
API_ACCESS_KEY = config("API_ACCESS_KEY")


app = FastAPI(lifespan=rate_limiter_lifespan)


@app.middleware("http")
async def custom_api_key_middleware(request: Request, call_next):
    # print(request.headers.get(API_KEY_HEADER))
    req_key_header = request.headers.get(API_KEY_HEADER)
    if f"{req_key_header}" != API_ACCESS_KEY:
        return JSONResponse(status_code=403, content={
            "detail": "Invalid Key"
        })
    response = await call_next(request)
    
    return response


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
    

@app.get("/predictions", dependencies=[Depends(RateLimiter(times=10, seconds=10))])
def list_pred_view():
    results = helpers.list_pred_results()
    
    return results
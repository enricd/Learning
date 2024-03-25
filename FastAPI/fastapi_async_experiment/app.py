# fastapi simple example

from fastapi import FastAPI
from time import sleep, time

app = FastAPI()

@app.get("/")
async def read_root():
    sleep(5)
    return {"Hello": "World"}


@app.get("/time")
async def read_time():
    sleep(5)
    return {"time": time()}



# in order to run the app, you need to run the following command
# uvicorn app:app --reload
# the first app is the name of the file, the second app is the name of the FastAPI instance
# --reload is used to reload the server when the code changes
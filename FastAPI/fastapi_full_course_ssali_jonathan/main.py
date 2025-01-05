from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}
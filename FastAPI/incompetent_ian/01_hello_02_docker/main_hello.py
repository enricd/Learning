import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main_hello:app", port=8000, reload=True)
    

# $ python main_hello.py 

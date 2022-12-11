from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Schema by pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# In memory simulated DB
my_posts = [{"id": 1, "title": "title of post 1", "content": "content of post 1"},
            {"id": 2, "title": "favorite foods", "content": "I like pizza"},
        ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
def root():                             # add async if needed
    return {"message": "Welcome to my api!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):    # title str, content str
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")     # {id} --> path parameter
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}

from typing import Optional
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

from .app_secrets import DB_USER, DB_PASSWORD

app = FastAPI()

# Schema by pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:

    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", 
                                user=DB_USER, password=DB_PASSWORD, 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!!")
        break

    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(3)


# In memory simulated DB
my_posts = [{"id": 1, "title": "title of post 1", "content": "content of post 1"},
            {"id": 2, "title": "favorite foods", "content": "I like pizza"},
        ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():                             # add async if needed
    return {"message": "Welcome to my api!!"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()

    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):    # title str, content str
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
                    (post.title, post.content, post.published))
                    # the %s in psycopg, in contrast to f-string, is not vulnerable to SQL injection
    new_post = cursor.fetchone()
    conn.commit()   # until now, changes were stagged, but in order to really put them into DB we need to commit

    return {"data": new_post}


@app.get("/posts/{id}")     # {id} --> path parameter
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    post = cursor.fetchone()
    conn.commit()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with the id: {id} does not exist")    

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
                    (post.title, post.content, post.published, str(id)))
    post = cursor.fetchone()
    conn.commit()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with the id: {id} does not exist")    

    return {"data": post}
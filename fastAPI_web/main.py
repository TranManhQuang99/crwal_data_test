from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # return published

    if published:
        return {'data': f'{limit} Quang'}

    else:
        return {'data': f'{limit} Sang'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished'}


@app.get("/blog/{id}")
def show_item(id: int):
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is create with {request.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from .models import PostCreate, CommentCreate, Post, Comment, PostWithComments
from .crud import create_post, get_post, update_post, delete_post, create_comment, list_posts, search_posts
from .middleware import timing_middleware, update_post_view_count
from typing import List, Dict

app = FastAPI()

app.middleware("http")(timing_middleware)

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Welcome to the Social App API"}

@app.post("/posts/", response_model=Post)
async def create_new_post(post: PostCreate):
    return await create_post(post)

@app.get("/posts/{post_id}", response_model=PostWithComments)
async def read_post(post_id: int, background_tasks: BackgroundTasks):
    post = await get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    background_tasks.add_task(update_post_view_count, post_id)
    return post

@app.put("/posts/{post_id}", response_model=Post)
async def update_existing_post(post_id: int, post_update: PostCreate):
    updated_post = await update_post(post_id, post_update)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@app.delete("/posts/{post_id}", response_model=Post)
async def delete_existing_post(post_id: int):
    deleted_post = await delete_post(post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post

@app.post("/comments/", response_model=Comment)
async def create_new_comment(comment: CommentCreate):
    return await create_comment(comment)

@app.get("/posts/", response_model=List[Post])
async def read_posts(skip: int = 0, limit: int = 10):
    return await list_posts(skip, limit)

@app.get("/search/", response_model=List[Post])
async def search(q: str):
    return await search_posts(q)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
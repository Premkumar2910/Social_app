from fastapi import Request
import time
from .database import db

async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

async def update_post_view_count(post_id: int):
    post = db.get_post(post_id)
    if post:
        post['view_count'] += 1
        db.update_post(post_id, post)
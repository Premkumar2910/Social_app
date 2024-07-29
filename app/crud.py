from .database import db
from .models import PostCreate, CommentCreate, Post, Comment, PostWithComments
from typing import List, Optional

async def create_post(post: PostCreate) -> Post:
    return Post(**db.add_post(post))

async def get_post(post_id: int) -> Optional[PostWithComments]:
    post = db.get_post(post_id)
    if post:
        comments = db.get_comments_for_post(post_id)
        return PostWithComments(**post, comments=comments)
    return None

async def update_post(post_id: int, post_update: PostCreate) -> Optional[Post]:
    updated_post = db.update_post(post_id, post_update)
    if updated_post:
        return Post(**updated_post)
    return None

async def delete_post(post_id: int) -> Optional[Post]:
    deleted_post = db.delete_post(post_id)
    if deleted_post:
        return Post(**deleted_post)
    return None

async def create_comment(comment: CommentCreate) -> Comment:
    return Comment(**db.add_comment(comment))

async def list_posts(skip: int = 0, limit: int = 10) -> List[Post]:
    return list(db.posts.values())[skip : skip + limit]

async def search_posts(query: str) -> List[Post]:
    return [post for post in db.posts.values() if query.lower() in post['title'].lower() or query.lower() in post['content'].lower()]
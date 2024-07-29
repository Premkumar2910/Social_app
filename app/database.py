from datetime import datetime

class Database:
    def __init__(self):
        self.posts = {}
        self.comments = {}
        self.post_id_counter = 1
        self.comment_id_counter = 1

    def add_post(self, post):
        post_id = self.post_id_counter
        self.post_id_counter += 1
        now = datetime.now()
        post_dict = post.dict()
        post_dict.update({
            "id": post_id,
            "created_at": now,
            "updated_at": now,
            "view_count": 0
        })
        self.posts[post_id] = post_dict
        return post_dict

    def get_post(self, post_id):
        return self.posts.get(post_id)

    def update_post(self, post_id, post_update):
        if post_id in self.posts:
            self.posts[post_id].update(post_update.dict(exclude_unset=True))
            self.posts[post_id]["updated_at"] = datetime.now()
            return self.posts[post_id]
        return None

    def delete_post(self, post_id):
        return self.posts.pop(post_id, None)

    def add_comment(self, comment):
        comment_id = self.comment_id_counter
        self.comment_id_counter += 1
        comment_dict = comment.dict()
        comment_dict.update({
            "id": comment_id,
            "created_at": datetime.now()
        })
        self.comments[comment_id] = comment_dict
        return comment_dict

    def get_comments_for_post(self, post_id):
        return [comment for comment in self.comments.values() if comment["post_id"] == post_id]

db = Database()
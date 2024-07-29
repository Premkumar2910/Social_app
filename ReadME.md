Social App API
This is a simple API for a social application, built with FastAPI. It provides basic CRUD operations for posts and comments, along with features like pagination, search, and view count tracking.

Features

Create, read, update, and delete posts
Add comments to posts
List posts with pagination
Search posts
Asynchronous operations
Custom middleware for request timing
Background tasks for updating post view counts

Requirements

Python 3.12
FastAPI
Uvicorn
Pydantic

Installation

1.git clone https://github.com/Premkumar/social-app-api.git
cd social-app-api

2.Create a virtual environment
python -m venv venv
 # On Windows, use `venv\Scripts\activate`

3.Install the required packages
pip install -r requirements.txt

4.To run the server:
uvicorn app.main:app --reload

API Endpoints

1.GET /: Welcome message
2.POST /posts/: Create a new post
3.GET /posts/{post_id}: Get a specific post
4.PUT /posts/{post_id}: Update a specific post
5.DELETE /posts/{post_id}: Delete a specific post
6.POST /comments/: Create a new comment
7.GET /posts/: List posts (with pagination)
8.GET /search/: Search posts

Development
This project uses an in-memory database for simplicity. In a production environment, you would want to replace this with a proper database.
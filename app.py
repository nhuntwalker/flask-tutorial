"""Quickstart Part 1: The Minimal Application."""
from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """The home page of the minimal flask application."""
    return "Index page!"


@app.route('/hello')
def hello() -> str:
    """Another page."""
    return "Hello world!"


@app.route('/user/<username>')
def show_user_profile(username: str) -> str:
    """Given a username, show that user's profile."""
    return f'{username}'


@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    """Show the post with the given id."""
    return f'Post {post_id}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next="/"))
    print(url_for('show_user_profile', username='John Doe'))

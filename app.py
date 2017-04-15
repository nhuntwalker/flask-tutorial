"""Quickstart Part 1: The Minimal Application."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """The home page of the minimal flask application."""
    return "Index page!"


@app.route('/hello')
def hello() -> str:
    """Another page."""
    return "Hello world!"

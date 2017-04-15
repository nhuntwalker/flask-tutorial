"""Quickstart Part 1: The Minimal Application."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """The home page of the minimal flask application."""
    return "Hello world!"

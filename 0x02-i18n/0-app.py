#!/usr/bin/env python3
"""
A simple Module that implements the /
route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """A function that displays a basic page"""
    return render_template('0-index.html')

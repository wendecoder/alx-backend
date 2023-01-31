#!/usr/bin/env python3
"""
A simple Module that implements the /
route
"""
from flask import Flask

app = flask(__name__)


@app.route('/')

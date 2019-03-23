from flask import Flask


def create_app(env=None):
    env = env or 'test'
    app = Flask(__name__)
    return app

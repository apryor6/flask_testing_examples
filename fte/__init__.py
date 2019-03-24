from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(env=None):
    env = env or 'test'
    app = Flask(__name__)
    db.init_app(app)

    @app.route('/health')
    def health():
        return jsonify('healthy')
    return app

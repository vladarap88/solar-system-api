from flask import Flask
from .db import db, migrate
from app.models import planet
from .routes.planet_routes import planets_bp


# def create_app(test_config=None):
def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(planets_bp)

    return app

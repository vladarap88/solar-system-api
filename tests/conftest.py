import pytest
from app import create_app
from app.routes.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.planet import Planet

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    planet_1 = Planet(
            name="Mercury",
            description="The smallest and closest planet to the Sun",
            distance_from_sun=36,
        )
    
    planet_2 = Planet(
            name="Venus",
            description="Similar in size to Earth",
            distance_from_sun=67,
        )

    db.session.add_all([planet_1, planet_2])

    db.session.commit()
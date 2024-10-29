from flask import Blueprint, abort, make_response, request
from app.routes.db import db
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.post("")
def create_planet():

    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance = request_body["distance"]

    new_planet = Planet(name=name, description=description, distance=distance)
    db.session.add(new_planet)
    db.session.commit()

    # response = new_planet.to_dict()
    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "distance": distance,
    }

    return response, 201


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.execute(query).scalars()

    planets_response = [
        {
            "id": planet.id,
            "name": planet.title,
            "description": planet.description,
            "distance": planet.distance,
        }
        for planet in planets
    ]

    return planets_response


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "distance": planet.distance,
    }


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet

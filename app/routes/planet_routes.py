from flask import Blueprint, abort, make_response, request
from app.routes.db import db
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.post("")
def create_planet():

    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance_from_sun"]

    new_planet = Planet(name=name, description=description, distance_from_sun=distance_from_sun)
    db.session.add(new_planet)
    db.session.commit()

    # response = new_planet.to_dict()
    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "distance_from_sun": distance_from_sun
    }

    return response, 201


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.execute(query).scalars()
    
    planets_response = [ {
        "id": planet.id,
        "name": planet.title,
        "description": planet.description,
        "distance": planet.distance_from_sun
    } 
    for planet in planets]
    
    return planets_response




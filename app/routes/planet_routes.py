from flask import Blueprint, abort, make_response, request
from .db import db
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.post("")
def create_planet():

    request_body = request.get_json()
    id = request_body["id"]
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance"]

    new_planet = Planet(name=name, description=description, distance_from_sun=distance_from_sun)
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
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



# @planets_bp.get("")
# def get_all_planets():

#     results_list = []

#     for planet in planets_list:
#         results_list.append(
#             {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "distance_from_sun": planet.distance_from_sun,
#             }
#         )

#     return results_list


# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "distance_from_sun": planet.distance_from_sun,
#     }


# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)

#     except ValueError:
#         response = {"message": f"Planet {planet_id} invalid"}
#         abort(make_response(response), 400)

#     for planet in planets_list:
#         if planet.id == planet_id:
#             return planet

#     response = {"message": f"Planet {planet_id} not found"}
#     abort(make_response(response), 404)

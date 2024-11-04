from flask import Blueprint, abort, make_response, request, Response
from app.routes.db import db
from app.models.planet import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.post("")
def create_planet():

    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance_from_sun"]

    new_planet = Planet(
        name=name, description=description, distance_from_sun=distance_from_sun
    )
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()

    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    name_param = request.args.get("name")

    if name_param:
        query = query.where(Planet.name == name_param)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    distance_from_sun_param = request.args.get("distance_from_sun")
    if distance_from_sun_param:
        query = query.where(Planet.distance_from_sun.ilike(f"%{distance_from_sun_param}%"))

    query = query.order_by(Planet.id)

    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response, 200

@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    response = planet.to_dict()

    return response, 200


@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return Response(status=204, mimetype="application/json")


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

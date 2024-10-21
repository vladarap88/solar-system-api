from flask import Blueprint, abort, make_response
from app.models.planet_models import planets_list


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.get("")
def get_all_planets():

    results_list = []

    for planet in planets_list:
        results_list.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance_from_sun": planet.distance_from_sun,
            }
        )

    return results_list


@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "distance_from_sun": planet.distance_from_sun,
    }


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)

    except ValueError:
        response = {"message": f"Planet {planet_id} invalid"}
        abort(make_response(response), 400)

    for planet in planets_list:
        if planet.id == planet_id:
            return planet

    response = {"message": f"Planet {planet_id} not found"}
    abort(make_response(response), 404)

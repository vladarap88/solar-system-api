from flask import Blueprint
from app.models.planet_models import planets_list


planets_bp = Blueprint("planets_bp", __name__, url_prefix ="/planets")

@planets_bp.get("")

def get_all_planets():

    results_list = []

    for planet in planets_list:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            distance_from_sun=planet.distance_from_sun
        ))

    return results_list




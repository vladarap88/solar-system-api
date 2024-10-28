# class Planet:
#     def __init__(self, id, name, description, distance_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun = distance_from_sun


# planets_list = [
#     Planet(
#         1, "Mercury", "The smallest and closest planet to the Sun", "36 million miles"
#     ),
#     Planet(2, "Venus", "Similar in size to Earth", "67 million miles"),
#     Planet(3, "Earth", "The only known planet to support life", "93 million miles"),
#     Planet(4, "Mars", "Known as the Red Planet", "142 million miles"),
#     Planet(5, "Jupiter", "The largest planet in the solar system", "484 million miles"),
#     Planet(6, "Saturn", "Famous for its beautiful ring system", "886 million miles"),
#     Planet(7, "Uranus", "An ice giant with a blue-green hue", "1.78 billion miles"),
#     Planet(8, "Neptune", "The farthest planet from the Sun", "2.8 billion miles"),
# ]

from sqlalchemy.orm import Mapped, mapped_column
from .routes.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun: Mapped[int]

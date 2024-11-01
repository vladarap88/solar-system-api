from sqlalchemy.orm import Mapped, mapped_column
from app.routes.db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun: Mapped[int]

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            distance_from_sun=self.distance_from_sun,
        )

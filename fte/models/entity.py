from fte import db


class Entity(db.Model):
    __tablename__ = "entities"
    entity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)

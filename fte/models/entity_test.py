from .entity import Entity
from fte.test.fixtures import app, db  # noqa


def test_add_entity(app, db):  # noqa

    # This is not a very useful test, as it basically is testing SqlAlchemy; however,
    # I leave it here as a reference for how to create objects
    with app.app_context():
        ENTITY_NAME = "My precious"
        obj = Entity(name=ENTITY_NAME)
        db.session.add(obj)
        db.session.commit()
        fetched = Entity.query.filter_by(name=ENTITY_NAME).all()
        assert len(fetched) == 1
        assert fetched[0].name == ENTITY_NAME


class DecoratorAndContext:
    def __enter__(self):
        print("ENTER!")
        return self

    def __exit__(self, c, e):
        print("EXIT")
        return self

    def __call__(self, f):
        print("DECORATING!")
        return f

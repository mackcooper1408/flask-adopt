from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """ Pet Model """

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable=False,
                          default='')
    age = db.Column(db.Text,
                    nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)


def example_data():
    pet1 = Pet(name="Fido",
               species="dog",
               photo_url="https://bit.ly/3nSubtf",
               age="puppy",
               available=True)

    pet2 = Pet(name="Jerry",
               species="cat",
               photo_url="https://bit.ly/3lLHee6",
               age="old",
               available=True)

    db.session.add_all([pet1, pet2])
    db.session.commit()


def connect_db(app):
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from app import app

    connect_db(app)

    db.drop_all()
    db.create_all()
    example_data()

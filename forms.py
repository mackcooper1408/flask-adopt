from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField


class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo Url")
    age = StringField("Age")
    available = BooleanField("Available")
    notes = StringField("Notes")

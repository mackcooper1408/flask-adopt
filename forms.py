from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species", validators=["dog","cat","porcupine"])
    photo_url = StringField("Photo Url",validators.URL)
    age = StringField("Age", validators=["baby", "young", "adult", "senior"])
    available = BooleanField("Available")
    notes = StringField("Notes")

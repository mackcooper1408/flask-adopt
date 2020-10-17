from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, ValidationError
from wtforms.validators import InputRequired, Optional, URL


def validate_species(form, field):
    if field.data not in ("cat", "dog", "porcupine"):
        raise ValidationError('Species must be cat, dog, or porcupine')


def validate_age(form, field):
    if field.data not in ("baby", "young", "adult", "senior"):
        raise ValidationError('Species must be a baby, young, adult or senior')


class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species", [InputRequired(), validate_species])
    photo_url = StringField("Photo Url", [URL()])
    age = StringField("Age", [InputRequired(), validate_age])
    available = BooleanField("Available")
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    photo_url = StringField("Pick A New Photo", [URL()])
    notes = StringField("Add Any Notes")
    available = BooleanField("Available")

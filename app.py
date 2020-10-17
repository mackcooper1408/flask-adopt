from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, RandPet
from forms import AddPetForm, EditPetForm
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

PETFINDER_API_KEY = "fZ8RVsdLN5bvZILZMsll5VTZXA4QTkSnBQhSBlp5lsGH8P1oMB"
PETFINDER_SECRET_KEY = "okkHwHlQFVuQKUQfzsRCIo4R8kcBrA7irTWRWCiT"

API_BASE_URL = "https://api.petfinder.com/v2/"

auth_token = str()

connect_db(app)

debug = DebugToolbarExtension(app)


@app.before_first_request
def refresh_credentials():

    global auth_token
    auth_token = update_auth_token_string()


@app.route('/')
def homepage():
    global auth_token
    pets = Pet.query.all()

    random_pets = get_pet_list()

    return render_template("homepage.html", pets=pets, random_pets=random_pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()
    # breakpoint()
    if form.validate_on_submit():
        new_pet = Pet(
                      name=form.name.data,
                      species=form.species.data,
                      photo_url=form.photo_url.data,
                      age=form.age.data,
                      notes=form.notes.data,
                      available=form.available.data
                      )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet_add.html", form=form)


@app.route("/<int:pet_id>", methods=["POST", "GET"])
def pet_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        # breakpoint()

        return redirect("/")

    else:
        return render_template("pet_details.html", pet=pet, form=form)


def update_auth_token_string():
    resp = requests.post("https://api.petfinder.com/v2/oauth2/token",
                         data={
                             "grant_type": "client_credentials",
                             "client_id": {PETFINDER_API_KEY},
                             "client_secret": {PETFINDER_SECRET_KEY}
                         })
    data = resp.json()
    # breakpoint()
    return data["access_token"]


def get_pet_list():
    resp = requests.get(f"{API_BASE_URL}/animals?limit=5",
                        headers={"Authorization": f"Bearer {auth_token}"})

    data = resp.json()

    pets = data["animals"]

    pet_list = list()
    for pet in pets:
        pet_list.append(RandPet(name=pet["name"],
                                species=pet["species"],
                                photo_url=(pet["photos"][0]["medium"]
                                           if pet["photos"]
                                           else 'https://bit.ly/2H547dC'),
                                age=pet["age"]))
    # breakpoint()

    return pet_list

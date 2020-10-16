from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

connect_db(app)

debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)


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
                      notes=form.notes.data
                      )
        db.session.add(new_pet)
        db.session.commit()
        # flash(f"Added {name} who a {age} {species}")
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)
@app.route("/<int:pet_id>")
def pet_details(pet_id):
    pet = Pet.query.get(pet_id)
    return render_template("pet_details.html",pet = pet)
@app.route("/<int:pet>/edit")
def pet_edit(pet_id):
    pet = Pet.query.get(pet_id)
    return re

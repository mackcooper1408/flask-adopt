from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
# from forms import PetAddForm

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

"""@app.route('/add', methods=["GET","POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        image = form.imageurl.data
        age = form.age.data
        notes = form.notes.data
        flash(f"Added {name} who a {age} {species})
        return redirect("/add")
    else:
        return render_template("snack_add_form.html" form = form)

    """

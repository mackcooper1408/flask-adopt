from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField
from models import db, connect_db, Pet

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
    
"""@app.route('/add')
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        image = form.imageurl.data
        age = form.age.data
    """

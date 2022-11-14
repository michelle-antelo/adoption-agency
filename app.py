from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://michelle:1003866Ma@localhost/pet_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "a secret!"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def render_homepage():
    return render_template("homepage.html")

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        flash(f"Successfully added {name}!")
        return redirect("/add", pets=['1', '2'])

    else:
        return render_template("add-pet-form.html", form=form)
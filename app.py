from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "a secret!"

debug = DebugToolbarExtension(app)

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
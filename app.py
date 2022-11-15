from flask import Flask, url_for, render_template, redirect, flash, jsonify, request
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.app_context().push()

app.config['SECRET_KEY'] = "a secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://michelle:1003866Ma@localhost/pet_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def list_pets():
    """Lists all pets in the homepage"""

    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data

        pet = Pet(
            name = name,
            species = form.species.data,
            photo_url = form.photo.data,
            age = form.age.data,
            notes = form.notes.data)

        db.session.add(pet)
        db.session.commit()

        flash(f"Successfully added {name}!")
        return redirect(f"/{pet.id}")
    elif form.name.data == None:
        return render_template("add-pet-form.html", form=form, edit=False)
    else:
        flash(f"Some or more of these inputs may be invalid.")
        return render_template("add-pet-form.html", form=form, edit=False)

@app.route('/<int:pet_id>')
def pet_display(pet_id):
    pet_data = Pet.query.get_or_404(pet_id)
    return render_template("pet-profile.html", pet_data=pet_data)

@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        name = form.name.data
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        flash(f"Successfully updated {name}!")
        return redirect(f"/{pet.id}")

    elif form.name.data == None: 
        flash(f"Unable to update {name}!")
        return redirect(f"/{pet.id}")

    else:
        return render_template("add-pet-form.html", pet=pet, form=form, edit=True)

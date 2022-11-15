from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, IntegerField
from wtforms.validators import AnyOf, NumberRange, URL

class AddPetForm(FlaskForm):
    """Add Pet Form"""

    name = StringField("Pet Name")
    species = StringField("Species", [AnyOf(["cat", "dog", "porcupine", "mouse", "parrot"])])
    photo = URLField("Photo URL", [URL()])
    age = IntegerField("Age", [NumberRange(0, 30, "Field must be 0-30")])
    notes = TextAreaField("Notes")
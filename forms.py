from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, URLField, IntegerField

class AddPetForm(FlaskForm):
    """Add Pet Form"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo = URLField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
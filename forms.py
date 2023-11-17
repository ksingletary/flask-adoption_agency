from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("What is your pet's name", validators=[InputRequired(message="Name can't be blank")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("'Ruff'ly what age is he/she", validators=[Optional()] and [NumberRange(min=0, max=30)])
    notes = StringField("Any other notes", validators=[Optional()])
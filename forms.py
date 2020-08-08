from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, AnyOf, URL, NumberRange


class Add_Pets_Form(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[AnyOf(
        ['cat', 'Cat', 'Dog', 'dog', 'porcupine', 'Porcupine'], message="Must be a cat, dog or porcupine")])
    photo_url = StringField("URL for Pet Photo", validators=[
                            Optional(), URL(message="Must be a valid URL")])
    age = FloatField("How old is the pet?", validators=[
                     Optional(), NumberRange(message="Age must be between 0 and 30")])
    notes = StringField("Pet Notes", validators=[Optional()])

    available = BooleanField("Is Available?")


class Edit_Pet_Form(FlaskForm):
    photo_url = StringField("URL for Pet Photo", validators=[
                            Optional(), URL(message="Must be a valid URL")])
    notes = StringField("Pet Notes", validators=[Optional()])

    available = BooleanField("Is Available?")

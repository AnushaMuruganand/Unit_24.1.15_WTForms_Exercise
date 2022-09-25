from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, SelectField, BooleanField

from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """ Class to create a pet form """ 
    name = StringField("Pet Name : ", validators = [InputRequired()])
    species = SelectField("Species of the Pet : ", choices = [('cat','cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField("Photo URL : ", validators = [Optional(), URL()])
    age = FloatField("Age : ", validators = [Optional(), NumberRange(min = 0, max = 30)])
    notes = TextAreaField("Comments : ", validators = [Optional(), Length(min = 10)])

class EditPetForm(FlaskForm):
    """ Class to edit an existing pet's details """
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")

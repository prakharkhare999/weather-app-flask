from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired  # Corrected this import

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])  # Corrected the validator
    submit = SubmitField("Submit")

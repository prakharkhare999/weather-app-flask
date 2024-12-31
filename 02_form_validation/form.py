from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    # name of variable=type(labelname,vaidaters)
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),])
    confirm_password=PasswordField("Confirm-Password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField("Sign Up")


class LoginForm(FlaskForm):
    # name of variable=type(labelname,vaidaters)
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired(),])
    remember=BooleanField('Remember me')
    submit=SubmitField("Login")

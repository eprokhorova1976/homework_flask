from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Name', validtors=[DataRequired()])
    surname = StringField('Surname', validtors=[DataRequired()])
    email = StringField('Email', validtors=[DataRequired(), Email()])
    password = PasswordField('Password', validtors=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Password confirm', validators=[DataRequired(), EqualTo('password')])

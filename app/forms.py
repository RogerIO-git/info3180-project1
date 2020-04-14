from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    bio = TextAreaField('Biography', validators=[DataRequired(), Length(min=5,max=200, message="Please enter a short biography.")])
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Only images can be uploaded')])
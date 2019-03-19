from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError,IntegerField,DateTimeField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User,Feedback
from flask_wtf.file import FileField,FileRequired
import phonenumbers

class RegistrationForm(FlaskForm):
    username = StringField('User Name',validators=[DataRequired(), Length(min=5, max=20)])
    fname = StringField('First Name',validators=[DataRequired(), Length(min=2, max=20)])
    mname = StringField('Middle Name',validators=[Length(min=2, max=20)])
    lname = StringField('Last name',validators=[Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    mobile=StringField('Mobile',validators=[DataRequired(),Length(10)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6,max=15)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')



    def validate_email(self,email):

        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email address already exist!')



class LoginForm(FlaskForm):
    username=StringField('User Name',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class FeedbackForm(FlaskForm):
    feed=StringField('Feedback',validators=[DataRequired()])
    submit = SubmitField('Submit')

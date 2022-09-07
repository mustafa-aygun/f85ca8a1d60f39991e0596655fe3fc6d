#It is the PickDate class file where DateField is used and definied to later use in front-end side to allow client pick a date to ask Exchange Rates.
from flask_wtf import FlaskForm
from datetime import date
from wtforms.fields import DateField
from wtforms import validators

class PickDate(FlaskForm):
    defaultDate = date.today() #Today is given as default date. 
    date = DateField('Date', default=defaultDate, validators=(validators.DataRequired(),))
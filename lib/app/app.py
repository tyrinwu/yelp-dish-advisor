"""Web application that hosts Yelp Dish Advisor


"""
import flask
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class YelpQueryForm(Form):
    """Handling query"""
    location = StringField("Location")
    preferences = StringField("Preferences. Divided by comman", validators=[Required()])
    submit = SubmitField("Search")

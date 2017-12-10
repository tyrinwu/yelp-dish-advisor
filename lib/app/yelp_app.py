"""Web application that hosts Yelp Dish Advisor


"""
import flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_script import Manager
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Should be something hard to guess'

manager = Manager(app)
bootstrap = Bootstrap(app)

class YelpQueryForm(FlaskForm):
    """Handling query"""
    location = StringField("Location")
    preferences = StringField("Preferences. Divided by comman", validators=[Required()])
    submit = SubmitField("Search")


@app.route('/', methods=['GET', 'POST'])
def index():
    location, preferences = None, None
    form = YelpQueryForm()
    if form.validate_on_submit():
        location = form.location.data
        preferences = form.preferences.data
        # If you want to clear the from uncomment the following
        # form.location.data = ""
        # form.preferences.data = ""
    return render_template('index.html', form=form, 
            preferences=preferences, location=location)


if __name__ == '__main__':
    manager.run()

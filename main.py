from flask import Flask
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html',  title='About')


@app.route('/certificate')
def certificate():
    return render_template('certificate.html')


@app.route('/coming')
def coming():
    return render_template('coming.html')


app.run(debug=True, host='0.0.0.0')

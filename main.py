from flask import Flask, request
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


@app.route('/certificate', methods=['post', 'get'])
def certificate():
    d1=0
    d2=0
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        print(username)
        d1 = request.form.get('date1')
        d2 = request.form.get('date2')
        print(d1)
        print(d2)

    return render_template('certificate.html')


@app.route('/coming')
def coming():
    return render_template('coming.html')


app.run(debug=True, host='0.0.0.0')

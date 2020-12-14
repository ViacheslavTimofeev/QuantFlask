from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


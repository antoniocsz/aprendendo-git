# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, request, url_for
from forms import Formulario

frontend = Blueprint('frontend',__name__)

#def index():
#    return render_template('index.html')

@frontend.route('/')
def home():
    return render_template('home.html')
    
@frontend.route('/login')
def login():
    form = Formulario()
    return render_template('login.html', form = form)

@frontend.route('/index', methods=['GET','POST'])
def index():
    if method.request == 'POST':
        return redirect(url_for('index'))
    return render_template('profile.html')

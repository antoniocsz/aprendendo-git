# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, request, url_for
import wtforms

frontend = Blueprint('frontend',__name__)

@frontend.route('/')
def home():
    return render_template('home.html')

@frontend.route('/login')
def login():
    return render_template('login.html')

@frontend.route('/index', methods=['GET','POST'])
def index():
    email = 'teste@teste.com'
    senha = 'teste123'
    if request.method == 'POST':
        username = str(request.form['username'])
        password = str(request.form['password'])
        print (username, password)
        if email != username or senha != password:
            print(True)
            return 'Erro 404'
        else:
            return render_template('index.html')

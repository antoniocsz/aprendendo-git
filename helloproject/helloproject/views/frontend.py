# -*- encoding:utf-8 -*-
from flask import Blueprint
from flask import render_template

frontend = Blueprint('frontend',__name__)

@frontend.route('/')
@frontend.route('/index')
def index():
	return render_template('index.html',)

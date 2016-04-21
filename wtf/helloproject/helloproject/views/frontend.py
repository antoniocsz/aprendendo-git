# -*- encoding:utf-8 -*-
from flask import Blueprint

frontend = Blueprint('frontend',__name__)

@frontend.route('/')
def index():
    return "<strong style='color:red; text-align:center'><h1>Olá,</h1></strong><br><br>Quem é o menino da vila?<br><br><br>R: Neymar!"

from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField, validators

class Formulario(Form):
    username = TextField('Login', [validators.Required('Insira login.'), validators.Length(min=4, max=30)])
    password = PasswordField('Senha', [validators.Required('Insira sua senha.'), validators.Length(min=6, max=16)])
    submit = SubmitField('Enviar')

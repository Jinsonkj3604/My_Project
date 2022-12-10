from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail




app=Flask(__name__)


app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet.db'


db = SQLAlchemy(app)
crypt = Bcrypt(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'sneha.fabstudioz@gmail.com'
app.config['MAIL_PASSWORD'] = 'SNEHAKRISHNA@2000'
app.config['MAIL_DEFAULT_SENDER'] = 'sneha.fabstudioz@gmail.com'
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_manager'


from My_project import routes
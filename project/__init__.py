import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret' #to allow us to use forms, not safe for deployment
app.config["TEMPLATES_AUTO_RELOAD"] = True

##########################################
############ DATABASE SETUP ##############
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

##########################################
######### REGISTER BLUEPRINTS ############
##########################################

from project.core.views import core
from project.clubs.views import clubs

app.register_blueprint(core)
app.register_blueprint(clubs)

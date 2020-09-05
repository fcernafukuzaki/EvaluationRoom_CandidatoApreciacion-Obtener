from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from os import environ
from common.DecimalEncoder import *

from flask_cors import CORS

DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
DATABASE_URI = DATABASE_URI[1:len(DATABASE_URI)-1]

# Aplicación de servidor
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.json_encoder = DecimalEncoder
db = SQLAlchemy(app)
api = Api(app)

CORS(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'NOTSOSECRETKEY'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/SLDB'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DatabaseParams


app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': DatabaseParams.sqlalchemy_uri,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

db = SQLAlchemy(app)

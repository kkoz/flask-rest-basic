from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)


from app import routes, models

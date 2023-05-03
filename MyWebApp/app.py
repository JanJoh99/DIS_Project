import os 
import psycopg2
from dotenv import load_dotenv
from flask import Flask 
from views import views
from auth import auth
from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app ():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] =f'postgresql+psycopg2://@janjohannsen/{DB_NAME}'
    db.init_app(app)
    # Register Blueprints
    
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
      
    return app 
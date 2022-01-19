# Import the Flask library to run the framework
from flask import Flask
# Import the SQL library to run the database structure
from flask_sqlalchemy import SQLAlchemy
# Import the path structure from the OS
from os import path
from flask_login import LoginManager

# Define a new database
# db is the database object when adding to the database
db = SQLAlchemy()
DB_NAME = "database.db"

# Here the function will initiate the application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5a#6lsd7jafa7&k5 akl!4;d4fK546JF*4NL;'
    
    # declare the SQL database in use
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initiate the database
    db.init_app(app)

    # Declare the views and auth created
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the database structure from the models.py
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Check if databse already exist and if not then it will create it
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
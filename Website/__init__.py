from flask import Flask #importing the flask module
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy() #creating object for the SQLAlchemy class
DB_NAME = "database.db" #name for the database

def create_app():   #function to import 
    app = Flask(__name__)   #initializing the app __name__ represents the file, used to initialize flask
    app.config['SECRET_KEY'] = 'S3CR3T_K3Y'     #this is going to encrypt the cookies or session data with a security key
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    #this to tell where the database needs to be created in the directory
    db.init_app(app)    #this is to initialize the database
    
    from .views import views    #to import the urls and their functions
    from .auth import auth      #same as above
    
    
    app.register_blueprint(views,url_prefix='/')    
    #this is to register the blueprints
    app.register_blueprint(auth,url_prefix = '/')   
    #this is to register the blueprints
    #we import the following to make sure that models.py file runs before we initialize or create our database
    
    from .models import User,Note

    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where do we need to go if the user is not logged in
    login_manager.init_app(app) #telliung the login manager which app we are using
    
    @login_manager.user_loader #telling flask how we load a user
    def load_user(id):
        return User.query.get(int(id)) 
        #this will look for the primary key by default
    
    return app #returning the flask app using this
    #we have now created a flask application and initialized a secret key

def create_database(app):
    if not path.exists('Website/'+DB_NAME):
        db.create_all(app = app)
        print("Created Database!")

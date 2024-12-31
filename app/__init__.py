from flask import Flask

#method which creates and return a Flask app instance
def create_app():

    #creating a Flask application instance
    app = Flask(__name__)

    #specifying the routes module for registering endpoints 
    from .routes import register_routes
    register_routes(app)

    return app
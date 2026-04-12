from flask import Flask

def create_app ():
    app = Flask(__name__)
    app.config ["SECRET_KEY"] = "placeholder_secret_key"
    # secret key 

    # import and register blueprints
    from website.views import views
    from website.auth import auth


    # register the blueprints with the Flask app
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")    


    # 

    # returns the Flask app instance
    return app

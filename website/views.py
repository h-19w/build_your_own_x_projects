from flask import Blueprint

views = Blueprint("views", __name__)
# from . import routes --- IGNORE ---

@views.route("/") # decorator to specify the URL for this view function
def home():
    return "<h1>Welcome to the Home Page!</h1>" # return a simple string as the response
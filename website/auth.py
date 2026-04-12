from flask import Blueprint

auth = Blueprint("auth", __name__)
# from . import routes --- IGNORE ---


@auth.route("/login") # decorator to specify the URL for this view function
def login():
    return "<h1>Login</h1>" # return a simple string as the response


@auth.route("/logout") # decorator to specify the URL for this view function
def logout():
    return "<h1>Logout</h1>" # return a simple string as the response


@auth.route("/signup") # decorator to specify the URL for this view function
def signup():
    return "<h1>Signup</h1>" # return a simple string as the response

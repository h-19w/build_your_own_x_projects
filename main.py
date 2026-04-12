from website.init import create_app

app = create_app()

if __name__ == "__main__":
    # if we run this file directly, start the Flask development server
    app.run(debug=True) #runs the flask app


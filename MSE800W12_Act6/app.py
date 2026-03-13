# import flask framework
from flask import Flask, render_template

# create flask application
app = Flask(__name__)

# home page
@app.route("/")
def home():
    return render_template("index.html")

# page that shows the image
@app.route("/show-image")
def show_image():
    return render_template("image.html")

# run the application
if __name__ == "__main__":
    app.run(debug=True)
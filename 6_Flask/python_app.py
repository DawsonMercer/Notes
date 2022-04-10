import csv
import datetime
import os
from flask import Flask, render_template, request, redirect, url_for

#cd 6_Flask
#venv\Scripts\activate
#$env:FLASK_APP = "python_app"
# $env:FLASK_ENV = "development"
#flask run

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

# @app.route("/")
# def hello_world():
#     now = datetime.datetime.now()
#     new_year = now.month == 3 and now.day == 21
#     return render_template("index.html", new_year=new_year)

@app.route("/photos")
def photos():
    # bicycle_images = ["bike1.jpg", "bike2.jpg", "bike3.jpg"]
    bicycle_images = []
    with open("photos.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            bicycle_images.append(row) # bicycle_images = []

    return render_template("photos.html", bicycle_images=bicycle_images)


@app.route("/dawson")
def name():
    name = "Dawson"
    return f"<h1>Hello, {name}!</h1>"

app.config["UPLOAD_PATH"] = "static/images"
@app.route('/upload', methods=["GET", "POST"])
def file_upload():
    if request.method == "GET":
        return render_template("image_upload.html")
    caption = request.form.get("caption")
    print(caption)
    uploaded_file = request.files["bicycle_image"]
    if uploaded_file.filename != "":
        uploaded_file.save(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], uploaded_file.filename))
        bicycle_images = []
        with open("photos.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                bicycle_images.append(row)
        bicycle_images.append([uploaded_file.filename, caption])
        with open("photos.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(bicycle_images)
    return redirect(url_for("photos"))



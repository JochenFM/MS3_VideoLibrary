import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint
from flask_paginate import Pagination, get_page_args
import random
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

mod = Blueprint('users', __name__)

# Pagination activity limit

PER_PAGE = 4


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("videos.html")


# Pagination
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
def paginated(videos):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE
    return videos[offset: offset + PER_PAGE]


def pagination_args(videos):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(videos)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


@app.route("/all_videos")
def all_videos():
    videos = list(mongo.db.videos.find())
    videos_paginated = paginated(videos)
    pagination = pagination_args(videos)

    return render_template(
        "library.html", videos=videos_paginated, pagination=pagination)


def get_suggested_videos(video_id):

    """
        Get random videos based on compared fields
        Finds all videos where compared fields match with provided video.
        Returns random sample.
        Parameter:
        string: video_id from videos collection field "_id".
        string: comp_field, name of the keyword to compare with.
        Int: number of random videos returned.
        Returns:
        list: dictionnary of random videos.
    """
    video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
    num_to_select = 3
    suggested_videos = list.random.sample(
                mongo.db.videos.find({video, num_to_select}))


    # pick 3 random from suggested list
    return random.sample("videos.html", suggested_videos=suggested_videos)
        

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    videos = list(mongo.db.videos.find({"$text": {"$search": query}}))
    return render_template("library.html", videos=videos)
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))

            else:
                # invalid password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_video", methods=["GET", "POST"])
def add_video():
    if request.method == "POST":
        video = {
            "category_name": request.form.get("category_name"),
            "video_title": request.form.get("video_title"),
            "video_author": request.form.get("video_author"),
            "video_description": request.form.get("video_description"),
            "video_venue": request.form.get("video_venue"),
            "date": request.form.get("date"),
            "video_link": request.form.get("video_link"),
            "created_by": session["user"]
        }
        mongo.db.videos.insert_one(video)
        flash("Video sucessfully added")
        return redirect(url_for("all_videos"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_video.html", categories=categories)


@app.route("/edit_video/<video_id>", methods=["GET", "POST"])
def edit_video(video_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "video_title": request.form.get("video_title"),
            "video_author": request.form.get("video_author"),
            "video_description": request.form.get("video_description"),
            "video_venue": request.form.get("video_venue"),
            "date": request.form.get("date"),
            "video_link": request.form.get("video_link"),
            "created_by": session["user"]
        }
        mongo.db.videos.update({"_id": ObjectId(video_id)}, submit)
        flash("Video sucessfully updated")

    video = mongo.db.videos.find_one({"_id": ObjectId(video_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_video.html", video=video, categories=categories)


@app.route("/delete_video/<video_id>")
def delete_video(video_id):
    mongo.db.videos.remove({"_id": ObjectId(video_id)})
    flash("Video successfully deleted")
    return redirect(url_for("all_videos"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New category added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category successfully updated")
        return redirect(url_for("get_categories"))
 
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category sucessfully deleted")
    return redirect(url_for("get_categories"))


# allows user to delete account when in session
# deletes user from user database
# deletes video from from database
# sends visual confirmation


@app.route("/delete_profile/<username_id>")
def delete_profile(video, username):

    mongo.db.videos.remove({"_id": ObjectId(video)})
    mongo.db.users.remove({"_id": ObjectId(username)})
    flash("Profile deleted")
    return redirect(url_for("register"))


# get selection of videos to display as featured videos in videos.html

# def get_featured_videos(cocktail_id, comp_field, count):


# to tell app where and how to run the application


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


# needs to be updated to debug = False prior to submission

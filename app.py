import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env

# ======== CONFIGURATION ======== #

app = Flask(__name__)

mod = Blueprint('users', __name__)

# Pagination activity limit

PER_PAGE = 4


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ======== UTILITY FUNCTIONS ======== #


# ======== HOME PAGE ======== #


"""
        To get random selection
        of videos from collection
        Returns random sample,
        credit to Tim Nelson
"""


@app.route("/")
@app.route("/index")
def get_suggested_videos():
    suggested_videos = (
        [video for video in mongo.db.videos.aggregate([
            {"$sample": {"size": 4}}])])

    return render_template("videos.html", suggested_videos=suggested_videos)


# ======== VIDEO LIBRARY PAGE ======== #


"""
        To implement Flask pagination extension
        based on PER_PAGE parameter of 4
        credit to
        https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
"""


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


"""
        To implement Flask pagination extension
        selects paginated videos from videos
        collection
"""


@app.route("/all_videos")
def all_videos():
    videos = list(mongo.db.videos.find())
    videos_paginated = paginated(videos)
    pagination = pagination_args(videos)

    return render_template(
        "library.html", videos=videos_paginated, pagination=pagination)


"""
       Allows the user to search for filtered options on library.html template
       by text input.
       Returns:
       template: library.html with filtered results
    """


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    videos = list(mongo.db.videos.find({"$text": {"$search": query}}))
    return render_template("library.html", videos=videos)


# ======== REGISTER PAGE ======== #


"""
        Displays register page to guest user and allows to create an account.
        Checks if username already exists to
        prevent duplication
        Stores informations from website form to MongoDB.
        Inserts a new entry in the users collection.
        Returns:
        template: redirect to profile.html if registration successful.
    """


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


# ======== LOGIN PAGE ======== #


"""
        Shows log in page and allows user to log in.
        Checks if the username exists in MongoDB collection of users.
        Informs user if registration is successful or not through
        flash messages.
        Returns:
        template: profile.html if the registration is successful.
        template: login.html if registration unsuccessful.
    """


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
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


# ======== PROFILE PAGE ======== #

"""
        Displays profile page with user informations to logged-in user.
        Fetches all user informations from MongoDB users collection.
        string: username from user collection field "username".
        Returns:
        template: profile.html.
    """


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# ======== LOGOUT PAGE ======== #


# Logs out registered user from account
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ======== ADD VIDEO PAGE ======== #

"""
        Allows registered user to submit a video to the website through
        a form.
        Allows all form fields to be sent to the MongoDB video collection
        and category collection.
        Inserts a new entry in the previously mentionned collections.
        Returns:
        template: all_videos.html after changes if user is logged in.
    """


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


# ======== EDIT VIDEO PAGE ======== #


"""
        Allows the user to edit their submitted videos through a form.
        Checks for video ID field in MongoDB to fetch all data.
        Displays all previously submitted data of the video.
        Fetches all new entries to database and update the fields
        when submitted in video library.
        Parameter:
        ObjectId: video_id from the cideo collection ObjectId field.
        Returns:
        template: edit_video.html before and after
        changes if the user is logged in.
    """


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


# ======== DELETE VIDEO ======== #

"""
        Allows user to delete videos.
        Removes video from database.
        Parameter:
        string: video_id from videos collection.
        Returns:
        template: redirects to library.html
    """


@app.route("/delete_video/<video_id>")
def delete_video(video_id):
    mongo.db.videos.remove({"_id": ObjectId(video_id)})
    flash("Video successfully deleted")
    return redirect(url_for("all_videos"))


# ======== CATEGORY PAGE ======== #

"""
        Displays all categories.
        Gets list of all categories in the MongoDB
        categories collection in alphab. order
        Returns:
        template: categories.html
    """


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ======== ADD CATEGORY PAGE ======== #


"""
        Allows admin to submit a category to the website through
        a form.
        Allows the form field to be sent to the MongoDB category collection
        Inserts a new entry in the previously mentionned collection.
        Returns:
        template: add_categories.html for admin
        before submitting.
        template: categories.html after submitting
    """


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


# ======== EDIT CATEGORY PAGE ======== #


"""
        Allows the admin to edit a category through a form.
        Checks for category ID field in MongoDB to fetch relative data.
        Displays previously submitted data regarding the category by admin.
        Sends update to field to category collection.
        Parameter:
        ObjectId: category_id from the category collection ID field.
        Returns:
        template: edit_categories.html for the admin
        before submitting changes
        template: categories.html after submitting changes.

    """


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


# ======== DELETE CATEGORY ======== #

"""
        Allows admin to delete categories.
        Deletes category from database.
        Parameter:
        string: category_id from category collection.
        Returns:
        template: redirects to categories.html
    """


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category sucessfully deleted")
    return redirect(url_for("get_categories"))


# ======== DELETE PROFILE ======== #


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


# tells app where and how to run the application


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

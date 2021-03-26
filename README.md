

THis is the env.py file, just in case it gets lost again:
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "T&eYic9UGY95F9|~AMyKlJ(5DliADY")
os.environ.setdefault("MONGO_URI", "mongodb+srv://JochenUser:J0chenUser666@myfirstcluster.ex33f.mongodb.net/videolibrary?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "videolibrary")



Modal code:

<!---->

    <!-- Modal Structure 
  <div id="delete_video" class="modal">
    <div class="modal-content">
      <h4>Delete this video?</h4>
      <p>Are you sure you want to delete this video? This cannot be undone</p>
    </div>
    <div class="modal-footer">
        <a href="#!" class="modal-close waves-effect waves-green btn-flat">Agree</a>
      <a href="{{ url_for('delete_video', video_id=video._id) }}" class="btn btn-danger">Delete</a>
    </div>
  </div-->
       


<!--Modal from Santé
<div class="modal fade" id="delete_video_{{video._id}}" tabindex="-1" role="dialog"
    aria-labelledby="delete_video_{{video._id}}" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered " role="document">
        <div class="modal-content rounded-0">
            <div class="modal-header">
                <h5 class="modal-title">Delete this video?</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                Are you sure you want to delete this cocktail? This will be deleted forever.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-warning text-white" data-dismiss="modal">Cancel</button>
                <a href="{{ url_for('delete_video', video_id=video._id)}}" class="btn btn-danger">Delete</a>
            </div>
        </div>
    </div>
</div-->




![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Table of Contents

- **[User Experience](#User-Experience)**
  - [Project Goals](#Project-Goals)
    - [User Stories](#User-Stories)
- **[Design](#Design)**
  - [Database](#Database)
    - [Indexes](#Indexes)
    - [Queries](#Queries)
      - [Browsing](#Browsing)
      - [Users](#Users)
      - [Searching](#Searching)
      - [Uploading](#Uploading)
      - [Administration](#Administration)
  - [Fonts](#Fonts)
  - [Colours](#Colours)
  - [Layout](#Layout)
- **[Features](#Features)**
  - [Existing Features](#Existing-Features)
  - [Future Features](Future-Features)
- **[Technologies](#Technologies)**
  - [Site architecture](#Site-architecture)
  - [Languages](#Languages)
  - [Libraries](#Libraries)
  - [Editors](#Editors)
  - [Tools](#Tools)
  - [Platforms](#Platforms)
- **[Testing](#Testing)**
- **[Source Control](#Source-Control)**
  - [Branches](#Branches)
  - [Github Desktop](#Github-Desktop)
- **[Deployment](#Deployment)**
  - [Database Deployment](#Database-Deployment)
  - [Deployment Platform](#Deployment-Platform)
- **[Credits](#Credits)**
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)

## User Experience

### Project Goals

The project goal is...

### User Stories

**General User**


- (US015) - As a general user I want to access the websites from my favourite equipment, such as smartphones, tablets, laptops or PCs, without loss of content.
- (US 0188) - As a general user I want to be able to navigate the website intuitively and with ease.
- (US 0188) - As a general user I want to find out more about the website on social media.
- (US001) - As a general user I want the website to make suggestions to me so I can be introduced to new content (concerning presentations in the history of science and technology)
- (US002) - As a general user I want to be able to see at a glance some of the available content in sufficient detail so I get an idea what is displayed.
- (US002) - As a general user I want to be able to get an idea what the videos are about prior to loading them in order for me to decide whether or not I want to proceed watching them.  
- (US014) - As a general user I want to receive clear feedback for my actions so I know what the consequences are and whether any further action is required.
  Also, it is good practice to include a confirmation step for deletion. 
- (US005) - As a general user I want to be able to filter videos based on duration so I can get content that fits my available time budget.
- (US 0188) - As a general user I want the possibility to register to the website.


**Registered User**

- (US012) - As a registered user I want to be able to log in my account with username and password.
- (US012) - As a registered user I want to get visual confirmation when I am logged in.
- (US008) - As a registered user I want to upload my own selection of video entries so that other users can benefit from them.
- (US012) - As a registered user I want to get visual confirmation when I added/deleted a video entry.
- (US010) - As a registered user I want to be able to edit or delete a video entry I have submitted so that I can improve or remove it.
- (US003) - As a general user I want to search videos by title and author so that I can find specific content that helps me satisfy my curiosity.
- (US004) - As a general user I want to search videos by category name so that I can group content of a specific kind which reflects my interest.
- (US010) - As a registered user I want to be able to edit my profile by adding a picture and relevant information.
- (US010) - As a registered user I want to be able to delete my profile.
- (US012) - As a registered user I want to get visual confirmation when I deleted my profile.
- (US006) - As....save videos for furture reference (not sure I can pull this off).


**Admin**
- (US013) - As an admin I want all of the above options but I would also like to be able to update content on the website and ensure it adheres to site rules.
- (US) - As an Admin I want to be able to create and delete video categories.
- (US) - As an Admin I want to be able to view how many users are registered on the website and delete users if necessary.
 







With the cancellation of all acacdemic conferences, symposia and workshops during the pandemic, presentations and other scholarly contributions 
have been delivered online, via Zoom and similar software program, leaving behind a growing video database. This project is an interactive database 
enabling users to store, retrieve, search, update, and delete recorded presentations in the history of science and technology. From what I gather from 
discussions in the field, there is a real need to collect and make available this archive at a single online space, for scholars to watch and learn. 
However, it is not only scholars who can benefit from this project, but also the wider interested public, which - with the turn to the digital format - has generally 
been more involved in a hitherto traditionally closed academic space. Hence also the interactive element in the project enabling users to upload (and delete) videos.
 


Initializing of Sidenav with JS, via https://www.youtube.com/watch?v=MaP3vO-vEsg&t=843s (12:18min):
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});




Coolors pallette: https://coolors.co/b22222-d84315-750075-030303-ffffff


Fatima for helping me realize that when flask pymongo was not found in gitpod/did not run on gitpod, 
it was due to the env.py file being deleted/had dispaared so that I was unable to load the MONGO-URI string from Heroku to flask. In the end, I reinserted the env.py as a whole.

Jo for helping me with slider: "For the images, remember you're working with Flask. Images on Flask need a url as follows", see https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files

Fellow student Sean Young for...

herschel, curie images from the Wellcome Collection https://wellcomecollection.org/

For image sizing in carousel:
https://stackoverflow.com/questions/50652298/how-to-resize-an-image-inside-of-a-materialize-css-slider-to-make-it-fit

check out responsive video container https://materializecss.com/media-css.html


Testing
As Flask is a framework, you will need to validate the HTML code using the URL to avoid false error flags due to jinja2. 



My attempt at binding data from MongoDB to the video library failed in that data got injected into videos.html rather than library.html, but the html for the video.html changes to 
that of the video library, and in the latter, a new card with image is created as it should but not in the right format.



in library.html:
{% if session.user|lower == video.created_by|lower %} needed to be injected outside of the antecedent <P></P> tags to function to show the edit and delete icons only if session user
is identical with video creator. Initially, this did not work but for another reason: the category_id I added in MongoDB lacked the underscore.




   <!--{% for video in videos %}
    {{ video.video_title }}<br>
    {{ video.category_name }}<br>
    {{ video.video_description }}<br>
    {{ video.video_venue }}<br>
    {{ video.video_author }}<br>
    {{ video.date }}<br>
    {{ video.video_link}}<br>
    {% endfor %}-->
<!--Featured Videos-->



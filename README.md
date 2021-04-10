
THis is the env.py file, just in case it gets lost again:
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "T&eYic9UGY95F9|~AMyKlJ(5DliADY")
os.environ.setdefault("MONGO_URI", "mongodb+srv://JochenUser:J0chenUser666@myfirstcluster.ex33f.mongodb.net/videolibrary?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "videolibrary")


















@app.route("/all_videos")
def all_videos():
    videos = list(mongo.db.videos.find())
    return render_template("library.html", videos=videos)














![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Video *Wunderkammer* - A History of Science Video Database

![alt text]( "Responsive sample")

**[Live demo](https://ms3-video-library.herokuapp.com/)**

---

<span id="top"></span>

## Table of Contents

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-overview">Overview</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#database-model">Database model</a>
- <a href="#features">Features</a>
  - <a href="#features-current">Existing Features</a>
  - <a href="#features-future">Future Features</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

<span id="context"></span>

## Context

With the cancellation of virtually all in-person acacdemic conferences, symposia and workshops during the pandemic, presentations and other scholarly contributions 
have been delivered online, via Zoom and similar software programs, leaving behind a growing video database. This video library intends to capture some of these precious recordings by 
enabling users to store, retrieve, search, update, and delete them. For practical reasons, its main focus is the History of science and technology, 
a field I am also most familiar with. *Wunderkammer* in my title, which literally means Cabinet of Wonder, but is better known as cabinet of curiosities in English, 
reflects that focus. *Wunderkammern* emerged in the 16th century and - mainly formed by members of the merchant class and early practitioners of science - 
were a collection of notable objects, similar to modern museums. Some of them also served as entertainment, and inspired by that use and purpose, this project intends to build a collection, not of corals, bones, or plant specimen,
but of history of science talks, symposia, and workshop presentations. 
From what I gather from discussions among historians of science in the relevant online communities and elsewhere, there is a real need to collect and make available this archive at a single online space, 
for scholars to watch and learn, but also to store, order and retrieve content at their convenience.
However, it is not only scholars who can benefit from this project, but also the wider interested public, which - with the turn to the digital format - has generally 
been more involved in a hitherto traditionally closed academic space. The project is developed in that spirit of greater accessibility, and aims to address everyone with an interest in the 
wonders of the history of science.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>
<span id="ux"></span>

## UX

<span id="ux-overview"></span>

### Overview

Video *Wunderkammer* adresses everyone who is looking to get an overview of the digital video content created in the history of science community and the wider public, especially
during the current pandemic. Users are looking for content to learn, educate and somehow enrich their lives, and that so from the comfort of their electronic device. 
All design decisions have been made with the following goals in mind:
- Accessibility
- Ease of use
- Responsiveness
- Visual appeal

<span id="ux-stories"></span>

### User stories

#### Overarching user expectations

- Consistent
- Easy to navigate
- Intuitive
- Responsive
- Secure
- Visually appealing

#### General User ####

- (US001) - As a general user I want to access the websites from my favourite equipment, such as smartphones, tablets, laptops or PCs, without loss of content.
- (US 002) - As a general user I want to be able to navigate the website intuitively and with ease.
- (US 003) - As a general user I want to find out more about the website on social media.
- (US004) - As a general user I want the website to make suggestions to me so I can be introduced to new content (concerning presentations in the history of science and technology)
- (US005) - As a general user I want to be able to see at a glance some of the available content in sufficient detail so I get an idea what is displayed.
- (US006) - As a general user I want to be able to get an idea what the videos are about prior to loading them in order for me to decide whether or not I want to proceed watching them.  
- (US007) - As a general user I want to receive clear feedback for my actions so I know what the consequences are and whether any further action is required.
- (US 009) - As a general user I want the possibility to register to the website.

#### Registered User ####

- (US010) - As a registered user I want to be able to log in my account with username and password.
- (US011) - As a registered user I want to get visual confirmation when I am logged in.
- (US012) - As a registered user I want to upload my own selection of video entries so that other users can benefit from them.
- (US013) - As a registered user I want to get visual confirmation when I added/deleted a video entry.
- (US014) - As a registered user I want to be able to edit or delete a video entry I have submitted so that I can improve or remove it.
- (US015) - As a registered user I want to be warned before I delete videos.
- (US016) - As a general user I want to search videos by title and author so that I can find specific content that helps me satisfy my curiosity.
- (US017) - As a general user I want to search videos by category name so that I can group content of a specific kind which reflects my interest.
- (US018) - As a general user I want to be able to filter videos based on duration so I can get content that fits my available time budget.
- (US019) - As a registered user I want to be able to edit my profile by adding a picture and relevant information.
- (US020) - As a registered user I want to be able to delete my profile.
- (US021) - As a registered user I want to get visual confirmation when I deleted my profile.

#### Admin ####
- (US022) - As an admin I want all of the above options but I would also like to be able to update content on the website and ensure it adheres to site rules.
- (US023) - As an Admin I want to be able to create and delete video categories.
- (US024) - As an Admin I want to be warned before I delete categories 
- (US025) - As an Admin I want to get visual confirmation when I deleted a category.
- (US026) - As an Admin I want to be able to view how many users are registered on the website and delete users if necessary.
 
<span id="ux-wireframes"></span>

### Wireframes

Wireframes created at the start of the project for **desktop** can be accessed [here](wireframes/), as well as the **data schema**.

Some of the noteworthy deviations from the plan include:

1. The Hero image was turned into a slider instead for greater visual appeal. 
2. Pagination was included in All Videos for more convenient navigation, better visual overview, and to reduce loading time.
3. Likes orginally included in my data schema, but not in the Balsamiq wireframes were not included due to time constraints, meaning link behind like buttons on video cards is dead.  
4. I began to code the profile page originally not wireframed but did not go beyond a rought outline due to time constraints
5. This includes profile image upload and storage functionality which is contained in my data schema but not yet implemented 
6. Video cards were revised following implementation of upload functionality and now do not include link to video, but edit and delete icons which link to edit video interface which was not originally wireframed 
7. Admin functionality was not planned in wireframes, but is implemented in basic form.

<span id="ux-design"></span>

### Design

The decision to use Materialize meant customisation was somewhat limited, but this was an acceptable compromise given the site's purpose of displaying user content clearly.  

#### Colours

I took one of Materialize's stock colours - initially #D84315 deep-orange darken-3 - as a base and used [Coolers](https://coolors.co/) to find a matching colour scheme for the site. The deep orange, however, proved both too dark to bring out contrast and too close to red to allow for visual user guidance, so I switched to 

![#ff8a65](https://via.placeholder.com/15/ff8a65/000000?text=+) #ff8a65 (deep-orange lighten-2), 

but kept the other components of the palette: 

![palette](wireframes/coolors_palette.png)

The color composition was inspired by one of the slider images, which I had already included in my wireframes - one print of William Heath's series March of the Intellect (1826). The print contains the matt grey-green and cream colours which are used througout this page and contrast well with the lightened orange. I used the hex values of the Materialize's named colour in any required custom CSS styling.

**Core**

Two bold shades of Materialize's orange were used for the core elements of the site, namely the Navbar and Footer, in combination with the grey-green for all other components. My aim was to generate a combination of colours which would fit the slider images - all colours of which are in pastel shade - and to maintain a contrast with the black text and light cream background.

**Cards** & **Buttons**

The combination between green/orange/cream was maintained throughout the entire site to ensure consistency and maintain a contrast between components and action buttons on cards, search bar, modals, date picker, pagination links, and forms.
The buttons have consistent colours with intuitive suggestions about their functions. Orange buttons against black description text were used throughout the page to signify action - the only exceptions being the delete and like  buttons/icons as well as the edit icon which I kept in an alert red and green respectively. 

**Transition and transformation**

To add to the physicality of all cards, video coallapsibles and containers, the Materialize `hoverable` classes were added, and the `waves-effect` class for some buttons. 

#### Fonts

[Londrina Solid](https://fonts.google.com/specimen/Londrina+Solid#about) is a solid font which gives a sense of modern typeset to bridge the rather historical content with the more contemporary format of digital recordings. Moreover, as is mentioned in the font description, Londrina for the creator represents "urban confusion". While I do not subscribe to confusion, I felt the general theme was in line with the overall theme of *Wunderkammer*, or cabinets of wonders, that these scholarly presentations about the history of science do represent. In that spirit, I was also drawn to typeface's context of creation "in the streets of Sao Paulo, Brazil".

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="database-model"></span>

### Database model

MongoDB's non-relational database structure makes sense for this type of site as there are only a few relationships between the various collections. My database model looks as follows: ![dataschema](wireframes/ms3_video_dataschema.png)
As can be seen, I originally planned with five collections - users, videos, liking, categories, and profile images - to order the relations between users and videos. My actual implementation deviates from this model in that the site due to time constraints operates with only three collections: users, categories, and videos. Profile images, that users should be able to upload, as well as the liking option for videos will have to be implemented at a later stage.    
Also, number of categories was substantially increased in the middle of the project to capture the broad scope of the history of science and technology as I envision it being captured in the video recordings.

 



#### Videos collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string|Can be updated by Admin|
|video_title|string|Video title as inserted by the user.|
|video_author |string|Presenter(s) as entered by the user|
|video_description|string|Brief abstract of video content used to flesh out cards on library and home pages.|
|date|string||
|video_duration|string|eventually not implemented as duration is shown on iframe of video |
|video_URL|string|This is the link stored in MongoDB to the video uploaded to Cloudinary. Inserted via callback function during upload process |
|original_website|string| eventually not implemented as I am yet to figure out Copyright and hosting issues |
|created_by|string| Added as user is logged in with their username. As users currently cannot change username, simpler to store as a string|

#### Categories collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string|The admin's chosen title of the category. Cannot only be changed by Admin|

#### Users collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string|Chosen by user on account creation. Cannot be changed.|
|password|string|Chosen by user on account creation and hashed using Werkzeug Security.|
|image|string|Profile pic chosen by user on account creation (not implemented yet)

#### Images collection

Initially, I anticipated that users would be able to upload a profile picture of their choice to be saved on another database program with a link being stored in MongoDB but due to time constraints, I was unable to implement this now.

#### Likes collection

Similarly, I anticipated that users would be able to 'like' particular videos, which will then be displayed on their respective profile page, but this will have to be implemented at a later stage as well. 

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>

## Features

<span id="features-current"></span>

### Existing Features

The site allows users to upload and watch new videos and edit existing ones (when logged in). Users can also search for videos based on title, description, and category. Now we can come back to some of the user stories mentioned above to see how the requirements have been met:

 

**1. Material design**

MaterializeCSS features:
- [Cards](https://materializecss.com/cards.html)
- [Forms](https://materializecss.com/text-inputs.html)
- [Collapsibles](https://materializecss.com/collapsible.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)
- [Tooltips](https://materializecss.com/tooltips.html)


**2. Secure passwords**

(US009) When registering to the site, the user's password is hashed so that it is not revealed to the database owner.

**3. CRUD functionality**

General users can:
- (US005) on load see some of the available content in "fatured videos".


Registered users can:
- (US012 & US013) upload videos of their choice which is then confirmed by a flash message.
- (US014) edit and delete their own videos.
- (US016) search videos by keywords appearing in video title, abstract or category to find specific content according to their own preferences.


The admin can:
- (US022) perform all of the actions a registered user can. 
- (US023) create new video categories and edit or delete existing ones.


**4. Feedback Mechanisms with User**

(US015 & 021) When the user or admin clicks to delete a video or category, a modal pops up to confirm they wish to do so to prevent accidental deletion.
The site provides a number of other feeback mechanisms:
Forms indicate required fields with warning messages on submit.
Forms provide validation warnings through colour cues and messages on the form field.
Tooltips on hover next to delete/edit and reset/search icons explain functionality.
Interactive site components react to user actions with hover cues (even although links such as 'likes' inactive as yet).



**5. Pagination**

The Video Library page (and any search applied) will limit the number of activities visible to 4 in order to reduce the number of vidoes loaded and keep the focus on the content. Any number of videos beyond that will be displayed on following pages accessible via the pagination links at the bottom of the page.


<span id="features-future"></span>

### Future Features

**1. User profile**

(US019-021) Finish the user profile I started so that users can 
- view all videos they have created in one place and easily edit or delete them,
- see their favoured videos in one place,
- upload a profile image to the stored in Cloudinary and add a short bio,
- delete their profile. 

**2. Admin rights**

The admin should get the additional abilities to:
- (US022) edit or delete any video on the site in case inappropriate content has been uploaded,
- (US023) delete categories from the Categories drop-down, with measures for preserving relational integrity for videos no longer associated with a category.

**3. Implement 'like' functionality**

To allow registered users to favour videos by wiring up the already existing heart icon on the video collapsible to MongoDB and back to the user's profile so that users can memorize videos they like and build a individual small video library in their profile.


**4. Embedd videos in HTML**

To replace the current iframes with a [Cloudinary self-hosted video player](https://cloudinary.com/documentation/video_player_how_to_embed) coded in HTML and JS to give me more control over the player and playback, including customization and better security against loading of malicious code on iframes. 


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="technologies"></span>

## Technologies Used

### Languages


- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) to style HTML and dynamic elements.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) is the markup language for the site layout.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) to create and manipulate the site's client-side dynamic elements.
- [Python](https://www.python.org/) for the backend server and running queries to the database.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) to generate HTML from site templates.


### Frameworks

- [Flask](https://palletsprojects.com/p/flask/) to simplify webserver tasks
- [Materialize](https://materializecss.com/) to aid in responsive design and conforming to the google material design language.

### Extensions and kits

- [Flask Paginate](https://pythonhosted.org/Flask-paginate/) to help implement simple pagination on library.html
- [Werkzeug](https://palletsprojects.com/p/werkzeug/) to manage the Web Server Gateway Interface.
- [Cloudinary](https://cloudinary.com/) to store and serve videos and handle video uploading.

### Project management

- [Balsamiq](https://balsamiq.com/wireframes/) to create the wireframes for this project.
- [GitHub](https://github.com/) to store the project repository and deploy the site
- [GitPod](https://gitpod.io/) for version control.
- [Heroku](https://www.heroku.com/about) is the deployment platform.
- [MongoDB](https://www.mongodb.com/) as backend database.
- [dbdiagram](https://dbdiagram.io/home)  to create Entity Relationship diagram of the database. 

### Tools

- [Am I Responsive?](http://ami.responsivedesign.is/) to generate images across different devices' screen sizes.
- [Autoprefixer](https://autoprefixer.github.io/) to ensure CSS compatibility across different browsers.
- [Coolers.co](https://coolors.co/ff8a65-f2c078-faedca-c1dbb3-7ebc89) to help create the color palette used across the site.
- [Favicon.io](https://favicon.io//) to create the video recorder icon in the browser tab.
- [Font Awesome](https://fontawesome.com/) for all (button) icons.
- [Google Fonts](https://fonts.google.com/) for the font of this site.


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="deployment"></span>

## Deployment






<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="testing"></span>

## Testing

Full details of testing can be found [here](TESTING.md).

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="credits"></span>

## Credits

### Tutorials / Resources

- Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))


In iframe allow class, "autoplay" needs to be deleted, otherwise videos start playing with every reload/visit of page.
<a href="{{ url_for('edit_video', video_id=video._id) }}" class="edit-interface align-item-right">
                        <i class="fas fa-edit tooltipped" data-position="bottom" data-tooltip="Edit"></i></a>
                    <a href="#delete_video_{{video._id}}" class="edit-interface modal-trigger center-align">
                        <i class="fas fa-trash tooltipped" data-position="right" data-tooltip="Delete"></i></a>
Good video for modals in materialize with JS:
https://www.youtube.com/watch?v=GAQoVIgjeZA
He uses data-target to target the modal id. I use href so might be worthwhile going over this video again in case modals do not work.
Data-target ="" goes with class of btn in this video, so I will have to see whether href="#delete_video_{{video._id}}" to id="delete_video_{{video._id}}"
works in my case.


Initializing of Sidenav with JS, via https://www.youtube.com/watch?v=MaP3vO-vEsg&t=843s (12:18min):
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});



For embedding the Cloudinary video player, I followed https://cloudinary.com/documentation/video_player_how_to_embed

Note When using both the Upload Widget and Video Player on the same page, the video player scripts must be loaded first to prevent any conflicts, see https://cloudinary.com/documentation/video_player_how_to_embed

To get the upload widget working, I followed https://cloudinary.com/documentation/upload_widget and Sean Young's code for his MS3 which he kindly shared helped in wiring up the upload button

Fatima for helping me realize that when flask pymongo was not found in gitpod/did not run on gitpod, 
it was due to the env.py file being deleted/had disappeared so that I was unable to load the MONGO-URI string from Heroku to flask. In the end, I reinserted the env.py as a whole.

Jo for helping me with slider: "For the images, remember you're working with Flask. Images on Flask need a url as follows", see https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files

Fellow student Sean Young for help with setting up the Cloudinary upload widget, explaining the concept of flask pagination extension, especially {{pagination.links}}, for pointing out that
a web-hosted video players plus iframes actually works without any JS scripts

Tim Nelson for trying to solve the console errors from the cloudinary video player which was taken up my Sean Young
and for helping me change the collapsible query selector in JS to select *all* collapsibles

Ed Young for sharing a beautiful and neat code for pagination by [mozillazg](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) and for pointing out that it works just as fine in
MaterializeCSS as in Bootstrap.
And also for his exemplary ReadMe file for his Self-Isolution project from which I learned how to create tables in Markdown syntax.
Fellow student Toto for sharing his code for the above pagination.

Cormac for help with accessing my mongo.db database in the get_suggested_videos function in app.py




https://www.youtube.com/watch?v=MaP3vO-vEsg&t=397s for help in implementing slider

check out responsive video container https://materializecss.com/media-css.html

March of Intellect by William Heath, ca. 1828 was downloaded from the digital collections of [The British Library](https://www.bl.uk/collection-items/march-of-the-intellect#)

Sir William Herschel and Caroline Herschel. Colour lithograph by A. Diethe, ca. 1896, downloaded from the [Wellcome Collections' image library](https://wellcomecollection.org/collections).

Newton by William Blake, 1795-c.1805, downloaded from [Tate](https://www.tate.org.uk/art/artworks/blake-newton-n05058
)
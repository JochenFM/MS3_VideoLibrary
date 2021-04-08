

THis is the env.py file, just in case it gets lost again:
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "T&eYic9UGY95F9|~AMyKlJ(5DliADY")
os.environ.setdefault("MONGO_URI", "mongodb+srv://JochenUser:J0chenUser666@myfirstcluster.ex33f.mongodb.net/videolibrary?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "videolibrary")
















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
  - <a href="#features-current">Current</a>
  - <a href="#features-future">Future</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>


<span id="context"></span>

## Context

With the cancellation of virtually all in-person acacdemic conferences, symposia and workshops during the pandemic, presentations and other scholarly contributions 
have been delivered online, via Zoom and similar software programs, leaving behind a growing video database. This video library intends to capture some of that precious knowledge by 
enabling users to store, retrieve, search, update, and delete recorded presentations. For practical reasons, its main focus is the History of science and technology, 
a field I am also most familiar with. *Wunderkammer* in my title, which literally means Cabinet of Wonder, but is better known as cabinet of curiosities in English, 
reflects that focus. *Wunderkammern* emerged in the 16th century and - mainly formed by members of the merchant class and early practitioners of science - 
were a collection of notable objects, similar to modern museums. Some of them also served as entertainment, and similarly, this project intends to build a collection, not of corals, bones, or plant specimen
but of history of science talks, symposia, and workshop presentations. 
From what I gather from discussions in the relevant online communities, there is a real need to collect and make available this archive at a single online space, 
for scholars to watch and learn, but also to order, store and retrieve content at their convenience.
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
- (US015) - As a general user I want to search videos by title and author so that I can find specific content that helps me satisfy my curiosity.
- (US016) - As a general user I want to search videos by category name so that I can group content of a specific kind which reflects my interest.
- (US017) - As a general user I want to be able to filter videos based on duration so I can get content that fits my available time budget.

- (US018) - As a registered user I want to be able to edit my profile by adding a picture and relevant information.
- (US019) - As a registered user I want to be able to delete my profile.
- (US020) - As a registered user I want to get visual confirmation when I deleted my profile.


#### Admin ####
- (US021) - As an admin I want all of the above options but I would also like to be able to update content on the website and ensure it adheres to site rules.
- (US022) - As an Admin I want to be able to create and delete video categories.
- (US020) - As an Admin I want to be warned before I delete categories 
- (US020) - As an Admin I want to get visual confirmation when I deleted a category.
- (US023) - As an Admin I want to be able to view how many users are registered on the website and delete users if necessary.
 
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

The decision to use Materialize meant customisation was somewhat limited, but this was an acceptable compromise given the site's purpose of displaying user content clearly. Judicious use of the framework's cards gives the site a solid and consistent feel which promotes the user content. 

#### Colours

[Coolers](https://coolors.co/) was used to find an appropriate colour scheme for the site, however the decision was made to default to Materialize's stock colours wherever possible, and to simply use the hex values of the framework's named colours in any required custom CSS styling.

**Core**

Two bold shades of Materialize's indigo were used for the core elements of the site, namely the Navbar, Footer and section headings. The aim was to have a neutral colour, not overly warm, to maintain a contrast with the white text and background.

- ![#3949ab](https://via.placeholder.com/15/3949ab/000000?text=+) #3949ab (indigo darken-1)
- ![#1a237e](https://via.placeholder.com/15/1a237e/000000?text=+) #1a237e (indigo darken-4)






 





Testing
As Flask is a framework, you will need to validate the HTML code using the URL to avoid false error flags due to jinja2. 



My attempt at binding data from MongoDB to the video library failed in that data got injected into videos.html rather than library.html, but the html for the video.html changes to 
that of the video library, and in the latter, a new card with image is created as it should but not in the right format. Solved by swapping the functions index() and add_videos() in how 
each connects to MongoDB


Customize Cloudinary widget I followed https://cloudinary.com/documentation/upload_widget#localization




in library.html:
{% if session.user|lower == video.created_by|lower %} needed to be injected outside of the antecedent <P></P> tags to function to show the edit and delete icons only if session user
is identical with video creator. Initially, this did not work but for another reason: the category_id I added in MongoDB lacked the underscore.




## Testing

Lighthouse was used to test the performance of the application on all pages on mobile and desktop.

The following reports were generated:


*videos.html - Home:*


* Performance: REDO as currently at 19%

* Accessibility: 74%

"iframe elements do not have a title"
"Image elements do not have [alt] attributes"

- I added a title to the iframe tags and all attributes to all img

"Links do not have a discernible name"

- This refers to social link icons and not quite sure what to make of it 


* Best Practices: 80

"Browser errors were logged to the console"
"Issues were logged in the Issues panel in Chrome Devtools"

- CHECK

* SEO: 83

"Document does not have a meta description" 

- I added _meta name="Description" content=""_ providing a summary of the page content. 

"Image elements do not have [alt] attributes"

- I added them


*Profile.html*


* Performance:73

"Does not use passive listeners to improve scrolling performance"

Adding 'touchstart', onTouchStart, {passive: true} to my event listener functions, as advised, threw up errors so I left it as it is.

"Image elements do not have explicit width and height"

As I use the MaterializeCSS class="circle responsive-img", I skipped that.



* Accessibility:95
* Best Practices:87 because of console errors
* SEO: 100

*Add_Video.html*

* Performance. 92
* Accessibility:80

"Form elements do not have associated labels"
That refers to the categories drop-down for which I do not see the option to add another "label for" tag so I left it.

"Links do not have a discernible name"

Again, in the footer

* Best Practices:93 because of console errors
* SEO: 89

"Document doesn't use legible font sizes"
- Let's check again after white etxt converted to black text, but this might concern font size only

"Tap targets are not sized appropriately"
added margin of 8px around category validate class


*edit_video.html*

* Performance: 94

remove unused CSS and JS 
* Accessibility: 84
"Links do not have a discernible name"
"Form elements do not have associated labels"
That refers to the categories drop-down for which a label for tag is already in place and adding another one does not make sense, especially as the category field is populated with 
data from mongoDB.
* Best Practices: 93
 issues with JS

* SEO: 98

I have a full stop under my category drop down which is not meant to be there
"
Tap targets are not sized appropriately"
Category drop down is overlaping with label text on open: need to put margin/padding


*Library.html*

The page loaded too slowly to finish within the time limit. Results may be incomplete.

* Performance: 81

"Does not use passive listeners to improve scrolling performance"
- see above


* Accessibility:85


"Buttons do not have an accessible name"

Added aria-label = "Center Align"

"Links do not have a discernible name"

As above, this concerns social links, but here also search and reset buttons. I added tooltips to them for better accessibility, but I do not know whether Lihgthouse rewards that.


* Best Practices:87 because of console errors

* SEO: 88

"Links are not crawlable"
This refers to two <a> tags from the {{pagination.links}} flask extension which I do not seem to be able to change

"Tap targets are not sized appropriately"

Refers to pagination links for which I now added margin and padding


*logout.html, Login.html, register.html*

* Performance: 94
* Accesibility: 96

"Links do not have a discernible name"

* Best Practices: 87 remove browser errors
* SEO: 100

*add_category.html*

* Performance: 93
* Accessibility: 93
"Links do not have a discernible name"

* Best Practices: 87
* SEO: 100


*edit_category.html*

* Performance: 93
* Accessibility: 81
"Links do not have a discernible name"
"Form elements do not have associated labels"
That refers to the categories drop-down for which a label for tag is already in place and adding another one does not make sense, especially as the category field is populated with 
data from mongoDB.

* Best Practices: 87
* SEO: 100


    Lighthouse report is now as [follows]() 




A few opportunities to improve Performance and Best Practices on all pages remain 
and will be addressed at a later stage:


* Performance of ...:  

"Eliminate render-blocking resources"

"Serve images in next-gen formats"

"Image elements do not have explicit width and height"

* Best Practices in both pages:

"Browser errors were logged to the console" which concerns an issue with _link rel="manifest" href="/site.webmanifest"_ which I was unable to resolve.


Initializing of Sidenav with JS, via https://www.youtube.com/watch?v=MaP3vO-vEsg&t=843s (12:18min):
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});




Coolors pallette: https://coolors.co/b22222-d84315-750075-030303-ffffff


For embedding the Cloudinary video player, I followed https://cloudinary.com/documentation/video_player_how_to_embed


Note When using both the Upload Widget and Video Player on the same page, the video player scripts must be loaded first to prevent any conflicts, see https://cloudinary.com/documentation/video_player_how_to_embed


To get the upload widget working, I followed https://cloudinary.com/documentation/upload_widget and Sean Young's code for his MS3 which he kindly shared helped in wiring up the upload button

Fatima for helping me realize that when flask pymongo was not found in gitpod/did not run on gitpod, 
it was due to the env.py file being deleted/had dispaared so that I was unable to load the MONGO-URI string from Heroku to flask. In the end, I reinserted the env.py as a whole.

Jo for helping me with slider: "For the images, remember you're working with Flask. Images on Flask need a url as follows", see https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files

Fellow student Sean Young for help with setting up the Cloudinary upload widget, explaining the concept of flask pagination extension, especially {{pagination.links}}, for pointing out that
a web-hosted video players plus iframes actually works without any JS scripts

Tim Nelson for trying to solve the console errors from the cloudinary video player which was taken up my Sean Young
and for helping me change the collapsible query selector in JS to select *all* collapsibles

Ed Young for sharing a beautiful and neat code for pagination by [mozillazg](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) and for pointing out that it works just as fine in
MaterializeCSS as in Bootstrap.
Fellow student Toto for sharing his code for the above pagination.

Cormac for help with accessing my mongo.db database in the get_suggested_videos function in app.py



herschel, curie images from the Wellcome Collection https://wellcomecollection.org/

https://www.youtube.com/watch?v=MaP3vO-vEsg&t=397s for help in implementing slider


check out responsive video container https://materializecss.com/media-css.html
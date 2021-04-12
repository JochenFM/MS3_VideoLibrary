
THis is the env.py file, just in case it gets lost again:
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "T&eYic9UGY95F9|~AMyKlJ(5DliADY")
os.environ.setdefault("MONGO_URI", "mongodb+srv://JochenUser:J0chenUser666@myfirstcluster.ex33f.mongodb.net/videolibrary?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "videolibrary")


https://stackoverflow.com/questions/30113116/overlaying-an-image-with-text-in-materialize-css

https://css-tricks.com/design-considerations-text-images/

https://www.slideteam.net/blog/11-hacks-to-make-text-over-images-more-readable-craft-a-stunning-slide


test video is from ???

















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Video *Wunderkammer* - A History of Science Video Database

![alt text](am_i_responsive.png "Responsive sample")

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
---


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

<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>
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

![#ff8a65](https://via.placeholder.com/15/ff8a65/000000?text=+) #ff8a65 (Coral or deep-orange lighten-2 in MaterializeCSS), 

but kept the other components of the palette: 

![palette](wireframes/coolors_palette.png)

The color composition was inspired by one of the slider images, which I had already included in my wireframes - one print of William Heath's series March of Intellect (1826). The print contains the matt grey-green and cream colours which are used througout this page, as, following Coolors' names, Tea Green/Dark Sea Green and Lemon Meringue/Gold Crayola. These contrast well with the lightened orange, or Coral. I used the hex values of the Materialize's named colour in any required custom CSS styling.

**Core**

Two bold shades of Materialize's orange were used for the core elements of the site, namely the Navbar and Footer, in combination with the grey-green for all other components. My aim was to generate a combination of colours which would fit the slider images - all colours of which are in pastel shade - and to maintain a contrast with the black text and gold crayola/lemon meringue background.

**Cards** & **Buttons**

The combination between green/orange/cream was maintained throughout the entire site to ensure consistency and maintain a contrast between components and action buttons on cards, search bar, modals, date picker, pagination links, and forms.
The buttons have consistent colours with intuitive suggestions about their functions. Orange buttons against black description text were used throughout the page to signify action - the only exceptions being the delete and like  buttons/icons as well as the edit icon which I kept in an alert red and green respectively. 

**Transition and transformation**

To add to the physicality of all cards, video coallapsibles and containers, the Materialize `hoverable` classes were added, and the `waves-effect` class for some buttons. 

#### Fonts

[Londrina Solid](https://fonts.google.com/specimen/Londrina+Solid#about) is a solid font which gives a sense of modern typeset to bridge the rather historical content with the more contemporary format of digital recordings. Moreover, as is mentioned in the font description, Londrina for the creator represents "urban confusion". While I do not subscribe to confusion, I felt the general theme was in line with the overall theme of *Wunderkammer*, or cabinets of wonders, that these scholarly presentations about the history of science do represent. In that spirit, I was also drawn to typeface's context of creation "in the streets of Sao Paulo, Brazil".

<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>

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
|category_name|string|The admin's chosen title of the category. Can only be changed by Admin|

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

<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>

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
- [Responsive Video Container](https://materializecss.com/media-css.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)
- [Tooltips](https://materializecss.com/tooltips.html)


**2. Intuitive Design**

 - (US002 & US004) In the Navbar the Video *Wunderkammer* brand takes users to the part of the app that allows user to get an overview, the index page with featured videos and options to log in.
- Familiar buttons and icons have been used across the site for commonly expected actions e.g. add, edit, delete, search, back.
- Flash messages confirm to the user when meaningful actions were performed i.e., logins and content changes.
- As a user might expect, modals appear to warn before content can be deleted.
- (US003) The footer contains links to all relevant social media.


**3. Responsiveness**

- (US001) Pages adapt to a variety of screen sizes thanks to the Materialize grid template and extensive testing in Chrome Dev Tools.
- Materialize CSS 'video-container responsive-video' and 'responsive-img' classes were used to make both resize responsively to page width.
- Where readability is compromised, content structure is modified to give more space to items (e.g. more margin or padding around icons, hide content on small devices etc.) 


**4. Secure passwords**

(US009) When registering to the site, the user's password is hashed so that it is not revealed to the database owner.

**5. CRUD functionality**

General users can:
- (US005) on load see some of the available content in "fatured videos".


Registered users can:
- (US012 & US013) upload videos of their choice which is then confirmed by a flash message.
- (US014) edit and delete their own videos.
- (US016) search videos by keywords appearing in video title, abstract or category to find specific content according to their own preferences.


The admin can:
- (US022) perform all of the actions a registered user can. 
- (US023) create new video categories and edit or delete existing ones.


**6. Feedback Mechanisms with User**

(US015 & 021) When the user or admin clicks to delete a video, profile, or category, a modal pops up to confirm they wish to do so to prevent accidental deletion.
The site provides a number of other feeback mechanisms:
Forms indicate required fields with warning messages on submit.
Forms provide validation warnings through colour cues and messages on the form field.
Tooltips on hover next to delete/edit and reset/search icons explain functionality.
Interactive site components react to user actions with hover cues (even although links such as 'likes' inactive as yet).



**7. Pagination**

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

In its current state, the Admin (user with username "Admin") has the same functionalities as a registered user, plus the ability to add and delete categories. For future development, the admin should get the additional abilities to:
- (US022) edit or delete any video on the site in case inappropriate content has been uploaded,
- (US023) delete categories from the Categories drop-down, with measures for preserving relational integrity for videos no longer associated with a category.
- Admin should be defined by superuser functionality, rather than by name "Admin"

**3. 404 and 500 error handling**

Custom pages for 404 and 500 errors need to be inserted for when something goes wrong, allowing user to return to the content with minimal disruption.


**4. Implement 'like' functionality**

To allow registered users to favour videos by wiring up the already existing heart icon on the video collapsible to MongoDB and back to the user's profile so that users can memorize videos they like and build a individual small video library in their profile.


**5. Embedd videos in HTML**

To replace the current iframes with a [Cloudinary self-hosted video player](https://cloudinary.com/documentation/video_player_how_to_embed) coded in HTML and JS to give me more control over the player and playback, including customization and better security against loading of malicious code on iframes. 

**6. Upload videos by link only and display the video in my HTML**

The upload widget in its current form already allows video upload by URL only, but I failed to subsequently display the video in my HTML. JS manipulation of the Cloudinary videoplayer mentioned under 5 will make this possible by allowing me to use the Cloudinary Javascript SDK to create a URL that, if included in my library.html, will show the video that was uploaded. 

**7. **A more refined video search by text to allow better combinations than the current "or" method**

A improved search functionality would also include a dropdown menu next to the search field to allow filter and display videos by category.

**8. More interactive and defensive programming features such as**

If video title already exists in database (upper or lowercase):
  -  Displays a Flash message alerting that video already exists.
  -  Redirect to Add Video page.

If categories are deleted, videos categorized with them need to be reassigned in some way.

If a logged-out user tries to edit a video (or tries to open url with brute force using /edit_video/video_id), they need to be redirected to Log In page with Flash message indicating that Login is required first.

Or, if a logged-in user tries to edit another user's video by brute force, they need to be redirected to the Video Library page with Flash message alerting "This video was added by another user and cannot be edited by you!"




<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>

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


<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>

<span id="deployment"></span>

## Deployment


### Database Deployment
The site uses a Mongodb database for data storage and retrieval. 

- The following collections were created:
  - videos
  - categories
  - users

Further prerequisites:

- Gitpod as the recommended Integrated Development Environmet (IDE) at Code Institute.
- Python3: In order to to run the application in combination with Flask.
- PIP3: To install all application imports (such as Flask, PyMongo etc.).
- A template folder: To link with the app routes.


### How to clone Video *Wunderkammer*

To clone this project from its [GitHub repository](https://github.com/JochenFM/MS3_VideoLibrary):

1. From the repository, click **Code**.
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository.
3. In your local IDE, open Git Bash.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type `git clone`, and paste the URL copied in Step 2.

```console
git clone https://github.com/JochenFM/MS3_VideoLibrary
```

6. Press Enter. Your local clone is created.
7. Create a file called env.py to hold your app's environment variables, which should contain the following:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-.ex33f.mongodb.net/<database_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database_name>")
```
8. The app can now be run locally using
```console
python3 app.py
```


### Deployment Platform

To deploy the app to Heroku from its [GitHub repository](https://github.com/JochenFM/MS3_VideoLibrary), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** (always with an uppercase P) using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub.
3. **Log In** to [Heroku](https://id.heroku.com/login).
4. Select **Create new app** from the dropdown in the Heroku dashboard.
5. Create a unique app-name ('ms3-video-library') and choose the region nearest to you. Then press **Create app**.
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. Scroll to **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the env.py file created earlier:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|MONGO_DBNAME|`<database name>`|
|MONGO_URI|mongodb+srv://`<username>`:<password>@`<cluster_name>`.ex33f.mongodb.net/`<database_name>`?|
|PORT|`5000`|
|SECRET_KEY|`<app secret key>`|



10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>



<span id="testing"></span>

## Testing


Full details of testing can be found [here](TESTING.md).



<span id="credits"></span>

## Credits

### Tutorials / Resources

- Code Institute Task Manager Project ([Tim Nelson](https://github.com/TravelTimN))

Good resources to initialize MaterializeCSS components with Javascript are:

- Oston Code Cypher on [Modals](https://www.youtube.com/watch?v=GAQoVIgjeZA)
- Traversy Media on [Sidenav](https://www.youtube.com/watch?v=MaP3vO-vEsg&t=843s) and some slider styling.


For embedding the Cloudinary upload widget, I followed [Cloudinary's documentation](https://cloudinary.com/documentation/upload_widget).

Similarly, there is good documentation for implementing the [video player](https://cloudinary.com/documentation/video_player_how_to_embed) 


### Acknowledgments


A number of Code Institute's tutors were of great help. Many thanks to:

- Fatima who at the initial stages of this project, helped me realize that the reason for why the application failed to run was because my env.py file had been deleted/had disappeared.
- Jo who altered me to how/where [Flask looks for images](https://stackoverflow.com/questions/28207761/where-does-flask-look-for-image-files).
- Ed Young for sharing a beautiful and neat code for pagination by [mozillazg](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) and for pointing out that it works just as fine in
MaterializeCSS as in Bootstrap. Ed also wrote an exemplary ReadMe file for his Self-Isolution project from which I learned how to create tables in Markdown syntax.
- Cormac who helped with accessing my mongo.db database in the get_suggested_videos function in app.py by correcting an error.
- Tim Nelson who shared his code for randmomly selecting items and who helped me change the collapsible query selector in JS to select *all* collapsibles so they worked properly across the site. He also tried to solve the console errors from the cloudinary video player.



Special thanks also to my fellow students on Slack, especially to:

- Sean Young who took up where Tim left and pointed out that a web-hosted video players plus iframes actually works without any JS scripts. Sean also 
kindly helped me with setting up the Cloudinary upload widget, to code the JS callback function to inject the Cloudinary video URL back into the upload form to be submitted to MongoDB.

- Toto kindly shared his code for the above-mentioned Flask pagination extension.

Some MS3s were a great inspiration for this project, especially Audrey Lloancy's [Cocktail App](https://sante-cocktail.herokuapp.com/), Sean Young's [Plum Recipes](https://sante-cocktail.herokuapp.com/).

Thanks also to my mentor [Adegbenga Adeye](https://github.com/deye9) for encouraging me to try and code a video library.


### Image Credits

Slider images:

- March of Intellect by William Heath, ca. 1828 was downloaded from the digital collections of [The British Library](https://www.bl.uk/collection-items/march-of-the-intellect#)

- Sir William Herschel and Caroline Herschel. Colour lithograph by A. Diethe, ca. 1896, downloaded from the [Wellcome Collections' image library](https://wellcomecollection.org/collections).

- Newton by William Blake, 1795-c.1805, downloaded from [Tate](https://www.tate.org.uk/art/artworks/blake-newton-n05058).


Default profile picture:

- Corey Schafer's Python Flask Tutorial: Full-Featured Web App Part 7 - [User Account and Profile Picture](https://youtu.be/803Ei2Sq-Zs) (in the description below the video).


Placeholder video clip:

- Big Buck Bunny (2008), taken from [Blender](https://www.blender.org/about/projects/) (free and open source).


### Disclaimer

This site was developed for educational purposes only and for fun.

<div align="right"><a style="text-align:right" href="#top">Go to index</a></div>
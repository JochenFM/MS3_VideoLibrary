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
This refers to two < a > tags from the {{pagination.links}} flask extension which I do not seem to be able to change

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


In iframe allow class, "autoplay" needs to be deleted, otherwise videos start playing with every reload/visit of page.
<a href="{{ url_for('edit_video', video_id=video._id) }}" class="edit-interface align-item-right">
                        <i class="fas fa-edit tooltipped" data-position="bottom" data-tooltip="Edit"></i></a>
                    <a href="#delete_video_{{video._id}}" class="edit-interface modal-trigger center-align">
                        <i class="fas fa-trash tooltipped" data-position="right" data-tooltip="Delete"></i></a>



# Wiki

The Encyclopedia Website is a Django-based web application designed to emulate the functionality of Wikipedia. It allows users to create, edit, search, and view encyclopedia entries on various topics. The entries are stored as Markdown files and converted to HTML for display.

[Demonstration video](https://youtu.be/0Uc_ri40oR4?si=aZdyWFgmlMoPa7k7)


## Installation

#### Clone repository
```
  git clone https://github.com/OmarSwailam/wiki.git
```

#### Create a virtualenv(optional)
```
  python3 -m venv venv
```

#### Activate the virtualenv
```
  .venv/scripts/activate
```
#### Install all dependencies
```
   pip install -r requirements.txt
```
#### Migrate DB changes
```
  python manage.py migrate
```
#### Run application
```
  python manage.py runserver
```

## Features
* Entry Page: Renders the content of encyclopedia entries.
* Index Page: Lists all encyclopedia entries with clickable links for direct access.
* Search: Enables users to search for entries by entering queries into the search box.
* New Page: Allows users to create new encyclopedia entries with titles and Markdown content.
* Edit Page: Permits users to edit existing entry content and save changes.
* Random Page: Redirects users to a random encyclopedia entry.
* Markdown to HTML Conversion: Converts Markdown content into HTML for display using python-markdown2.

Author: Omar Swailam
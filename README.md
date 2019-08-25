# Neighbourhood
A Django python application that allows users to know what is happening in their particular neighborhood.

#### By **Philip Kariuki**


## Description
The objective here is to create an application that allows its user to to be in the loop about everything happening in your neighborhood.

Live link : https://welcometoomyhood.herokuapp.com

## User Stories
As a user, I would like to be able to do the following:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
| Display all posts for selected neighbourhood | On home page load | Loads all the available posts for chosen neighbourhood |
| New User Post | Click New Post button from navbar | User redirected to new post page with forms for new post, which when filled redirects to home page with the new post  |
| User registration | Fill required fields and click on register button | User's info is registered to the database and user is redirected to home page |
| User login | Fill required fields and click on login button | User's info is confirmed with the database and user is redirected to home page, else if info doesn't match db records user is not able to login and access the home page |
| Move to a different neighbourhood | From dropdown list select desired neighbourhood | User is switched to a different neighbourhood and can only see posts for that neighbourhood |

## Setup/Installation Requirements
To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/neighbourhood/
        $ cd /neighbourhood

To create and activate the virtual environment and install pip:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python


To install all the required pip modules for proper functionality:

        (virtual)$ python3.6 -m pip install -r requirements.txt

To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
To run unittests:

        $ python3.6 manage.py test hoodsapp

## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Django v 2.2.3
* Bootstrap4
* Django-registration v 3.0.1
* Postgres Database
* gunicorn


## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## Support and contact details
To support me, you can contact me at <a href="https://www.gmail.com">philippokar@hotmail.co.uk</a>

## License
[MIT © 2019](https://github.com/philipkariuki/neighbourhood/blob/master/LICENSE)

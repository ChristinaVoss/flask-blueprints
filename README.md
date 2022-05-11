# Flask Blueprints

This repo ties together much of what has been demonstrated in the other Flask demonstrations, such as [Flask templates](https://github.com/ChristinaVoss/flask-templates), [Flask forms](https://github.com/ChristinaVoss/flask-forms), and [Flask models](https://github.com/ChristinaVoss/flask-models). Here however, it is all structured and tied together using blueprints - making the app easier to maintain and expand.

### App structure

**Top level (in flask-blueprints folder)**

At the top level of the app we have app.py, which is now only used to run the app. There is also an added directory "project" to hold all the actual logic of the application. Flask migrate auto-creates a "migrations" directory that we don't manually update/touch so just ignore it (and any pycache, .sqlite or .git files).

**In project directory**

Our app now consists of:

- A clubs directory (the "clubs" blueprint - holds all code related to clubs)
- A core directory (holds all code to common/core elements)
- An `__init__.py` file (where the app and database is configured and blueprints are registered)
- A sqlite file (ignore, but keep)


**In clubs directory**

The clubs blueprint. An extension to the app that includes:

- A templates directory (for all templates related to clubs)
- An empty `__init__.py` file (needed by Flask to know that it needs to add this part to the app)
- A forms.py file for all club related forms
- A models.py file for all club related models
- A views.py file for the controllers (they define what the views (templates) will display). Define the blueprint here.

**In core directory**

The core blueprint. An extension to the app that includes:

- A templates directory (for all templates and parts that will be shared across the app)
- An empty `__init__.py` file (needed by Flask to know that it needs to add this part to the app)
- A views.py file for the controllers (they define what the views (templates) will display). Define the blueprint here.


### Setup

If you have not installed Python3, [please do](https://www.python.org/downloads/).

First create and activate some form of environment to store your dependencies. I like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html):

```
$ conda create -n myenv python=3.7

$ conda activate myenv
```

**Or** just use Pythons built in environments:

```
$ python3 -m venv venv

$ . venv/bin/activate
```

Then install Flask, Flask-SQLAlchemy, Flask-Migrate, and also WTForms (because we added a form to update the database).

`$ pip install Flask Flask-WTF Flask-SQLAlchemy Flask-Migrate`

### Run the app

`$ flask run`

You should now be able to see the output in your browser window (at http://127.0.0.1:5000) 

### Resulting pages

# Flask Blueprints

This repo ties together much of what has been demonstrated in the other Flask demonstrations, such as [Flask templates](https://github.com/ChristinaVoss/flask-templates), [Flask forms](https://github.com/ChristinaVoss/flask-forms), and [Flask models](https://github.com/ChristinaVoss/flask-models). Here however, it is all structured and tied together using blueprints - making the app easier to maintain and expand.

### App structure

<img width="695" alt="Screenshot 2022-05-12 at 09 31 21" src="https://user-images.githubusercontent.com/20923607/168027609-de48ccd7-fb77-4e9b-bac3-ed6aa4523110.png">

**Key parts**

app.py is now just the entry point to the app, and all code related to making the app is placed in a project directory. Because we no longer configure everything at top level, Flask will look for an `__init__.py` file inside project directory. We'll place all the configurations for our app there. We then have a clubs directory, which holds the 'clubs' blueprint, and a core directory for the 'core' blueprint.

In clubs/views.py

Import your required methods from flask, including the Blueprint contstructor:

`from flask import render_template, url_for, redirect, Blueprint`

Import your configured database (when you look in a directory, like 'project', Flask will look for the `__init__.py file):

`from project import db`

Then import any models and forms you may have in this blueprint directory:
```
from project.clubs.models import Club
from project.clubs.forms import CreateClub
```

Fianlly, define your blueprint (and if you have a template folder in your blueprint as we have in this example, tell flask where to find it with 'template_folder='):

`clubs = Blueprint('clubs', __name__, template_folder='templates')`

Now you use @clubs.route() instead of @app.route() in this blueprint. Do the same for the core blueprint, or any other your define.


In `__init__.py`:

Import and register the blueprints to the app:

```
from project.core.views import core
from project.clubs.views import clubs

app.register_blueprint(core)
app.register_blueprint(clubs)
```

In app.py:

Import the app so that you can run it:

`from project import app`

And that's it! Now you have a fully modularised app. In most demos and tutorials, the templates and models are kept outside the blueprints, but I thought it could be useful to see them fully encapsulated, so that they truly are mini-apps that extend your app, rather than have some of their code in the blueprint, and some out.

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

**index.html**

<img width="516" alt="Screenshot 2022-05-12 at 18 12 32" src="https://user-images.githubusercontent.com/20923607/168131471-ef14e357-2046-45be-b93f-afdd408114a4.png">

**create_club.html**

<img width="517" alt="Screenshot 2022-05-12 at 18 12 43" src="https://user-images.githubusercontent.com/20923607/168131487-d1b2c3e3-7472-4aea-a110-d318c3946783.png">


**clubs.html**

<img width="518" alt="Screenshot 2022-05-12 at 18 13 00" src="https://user-images.githubusercontent.com/20923607/168131506-962c56fe-e12e-487e-a344-10bbb5291a11.png">



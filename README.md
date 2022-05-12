# Flask Blueprints

This repo ties together much of what has been demonstrated in the other Flask demonstrations, such as [Flask templates](https://github.com/ChristinaVoss/flask-templates), [Flask forms](https://github.com/ChristinaVoss/flask-forms), and [Flask models](https://github.com/ChristinaVoss/flask-models). Here however, it is all structured and tied together using blueprints - making the app easier to maintain and expand.

### App structure

<img width="713" alt="Screenshot 2022-05-12 at 09 29 26" src="https://user-images.githubusercontent.com/20923607/168027313-700ed7d1-9537-4cf0-bd02-f500dd4fb6f2.png">



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

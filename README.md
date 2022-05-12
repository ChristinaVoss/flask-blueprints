# Flask Blueprints

This repo ties together much of what has been demonstrated in the other Flask demonstrations, such as [Flask templates](https://github.com/ChristinaVoss/flask-templates), [Flask forms](https://github.com/ChristinaVoss/flask-forms), and [Flask models](https://github.com/ChristinaVoss/flask-models). Here however, it is all structured and tied together using blueprints - making the app easier to maintain and expand.

### App structure

<img width="695" alt="Screenshot 2022-05-12 at 09 31 21" src="https://user-images.githubusercontent.com/20923607/168027609-de48ccd7-fb77-4e9b-bac3-ed6aa4523110.png">



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



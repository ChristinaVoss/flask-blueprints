from flask import render_template, url_for, redirect, Blueprint
from project import db
from project.clubs.models import Club
from project.clubs.forms import CreateClub

clubs = Blueprint('clubs', __name__)

# CREATE NEW CLUB
@clubs.route('/create_club.html', methods=['GET', 'POST'])
def create_club():
    form = CreateClub()

    if form.validate_on_submit():


        club = Club(name = form.name.data,
                    description = form.description.data)

        db.session.add(club)
        db.session.commit()

        return redirect(url_for('clubs.list_clubs'))
    return render_template('clubs/create_club.html', form=form)

@clubs.route('/list_clubs')
def list_clubs():
    clubs_list = Club.query.all()
    return render_template('clubs/clubs.html', clubs_list=clubs_list)

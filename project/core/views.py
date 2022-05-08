from flask import render_template, url_for, redirect, Blueprint

core = Blueprint('core', __name__)

# CREATE NEW CLUB
@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('core/index.html')

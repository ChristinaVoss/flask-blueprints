from flask import render_template, url_for, redirect, Blueprint

core = Blueprint('core', __name__, template_folder='templates')

# CREATE NEW CLUB
@core.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

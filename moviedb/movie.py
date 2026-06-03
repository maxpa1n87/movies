from flask import (
    Blueprint, render_template
)
from werkzeug.exceptions import abort
from datetime import datetime
from flask_login import login_required

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    return render_template('movie/index.html')

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    pass

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    pass

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    pass

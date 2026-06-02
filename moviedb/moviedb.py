from flask import (
    Blueprint, render_template
)
from werkzeug.exceptions import abort
from datetime import datetime
from flask_login import login_required
from flask import current_app

bp = Blueprint('moviedb', __name__)

@bp.route('/')
def index():
    db = get_db(current_app)
    movies = db.session.execute(db.select(User).order_by(User.username)).scalars()
    today = datetime.today().strftime("%d.%m.%Y")
    return render_template('moviedb/index.html', movies=movies, today=today)

@bp.route('/create')
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

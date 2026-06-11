from flask import (
    Blueprint, render_template, request, flash, redirect, url_for
)
from werkzeug.exceptions import abort
from datetime import datetime
from flask_login import login_required
from moviedb.shared.models import db
from moviedb.movies.models import Movie
from sqlalchemy.exc import IntegrityError

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    movies = db.session.execute(db.select(Movie)).scalars()
    today = datetime.today().strftime('%d.%m.%Y')
    return render_template('movie/index.html', movies=movies, today=today)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        description = request.form['description']
        author = request.form['author']
        release = request.form['release']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            try:
                release_date = datetime.strptime(release, '%Y')
                movie = Movie(title=title, subtitle=subtitle, description=description, author=author, release=release_date)
                db.session.add(movie)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                error = f"Movie {title} already exsist."
            except Exception as e:
                db.session.rollback()
                error = f"Release date must be only the year with 4 digits."
            else:
                return redirect(url_for('movie.index'))
            
        if error is not None:
            flash(error)

    return render_template('movie/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    pass

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    pass

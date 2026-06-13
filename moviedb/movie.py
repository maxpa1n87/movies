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
    page = db.paginate(db.select(Movie), max_per_page=5)
    return render_template('movie/index.html', page=page)

@bp.route('/search')
def search():
    page = None
    search_string = request.args.get('search_string')
    if search_string is not None:
        page = db.paginate(db.select(Movie).where(Movie.title == search_string), max_per_page=5)
    return render_template('movie/index.html', page=page)

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
            error = {'movie_title_is_required' : 'Title is required.' }

        if error is not None:
            flash(error)
        else:
            try:
                release_date = datetime.strptime(release, '%Y-%m-%d')
                movie = Movie(title=title, subtitle=subtitle, description=description, author=author, release=release_date)
                db.session.add(movie)
                db.session.commit()
            except ValueError as e:
                db.session.rollback()
                error = { 'movie_date_time_invalid' : 'Release date must be in the format YYYY.MM.DD' }
            except IntegrityError as e:
                db.session.rollback()
                error = { 'movie_title_is_invalid' : f"Movie {title} already exsist." }
            else:
                return redirect(url_for('movie.index'))
            
        if error is not None:
            flash(error)

    return render_template('movie/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    movie = db.get_or_404(Movie, id)

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
                movie.title = title
                movie.subtitle = subtitle
                movie.description = description
                movie.author = author
                movie.release = datetime.strptime(release, '%Y-%m-%d')
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

    return render_template('movie/update.html', movie=movie)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    movie = db.get_or_404(Movie, id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('movie.index'))

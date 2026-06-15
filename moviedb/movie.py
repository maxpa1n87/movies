from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, current_app
)

from datetime import datetime
from flask_login import login_required
from moviedb.shared.models import db
from moviedb.movies.models import Movie
from sqlalchemy.exc import IntegrityError
from moviedb.shared.utils import upload_file, delete_old_file

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    page = db.paginate(db.select(Movie), max_per_page=current_app.config['MAX_PAGES_PER_PAGE'])
    return render_template('movie/index.html', page=page)

@bp.route('/search')
def search():
    page = None
    search_string = request.args.get('search_string')
    if search_string is not None:
        page = db.paginate(db.select(Movie).where(Movie.title == search_string), max_per_page=current_app.config['MAX_PAGES_PER_PAGE'])
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
        new_filename = None

        if not title:
            error = {'movie_create_invalid_title' : 'Title is required.' }

        if not subtitle:
            error = {'movie_create_invalid_subtitle': 'Subtitle is required.' }

        if not description:
            error = {'movie_create_invalid_description': 'Description is required.' }

        if not author:
            error = {'movie_create_invalid_author': 'Author is required.' }
        
        if not release:
            error = {'movie_create_invalid_release': 'Release is required.' }

        existing_movie = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()

        if existing_movie is not None:
            error = {'movie_create_movie_already_exists': f'The movie with the title {title} already exists.' }

        if error is not None:
            flash(error)
        else:
            try:
                new_filename = upload_file(request, 'image')
                release_date = datetime.strptime(release, '%Y-%m-%d')
                movie = Movie(title=title, 
                              subtitle=subtitle, 
                              description=description, 
                              author=author, 
                              release=release_date, 
                              image=new_filename)
                db.session.add(movie)
                db.session.commit()
            except ValueError as e:
                db.session.rollback()
                error = { 'movie_create_value_error' : f'A value error occured. {e}' }
            except IntegrityError as e:
                db.session.rollback()
                error = { 'movie_create_integrity_error' : f"A integrity error occured. {e.code}" }
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
            error = {'movie_update_invalid_title' : 'Title is required.' }

        if not subtitle:
            error = {'movie_update_invalid_subtitle' : 'Subtitle is required.' }

        if not description:
            error = {'movie_update_invalid_description' : 'Description is required.' }

        if not author:
            error = {'movie_update_invalid_author' : 'Author is required.' }

        if not release:
            error = {'movie_update_invalid_release' : 'Release is required.' }

        # existing_movie = db.session.execute(db.select(Movie).where(Movie.title == title)).scalar()

        # if existing_movie is not None:
        #    error = {'movie_update_movie_already_exists' : f'The movie with the title {title} already exists.' }

        if error is not None:
            flash(error)
        else:
            try:
                new_image = upload_file(request, 'image')
                if new_image is not None:
                    delete_old_file(movie.image)
                movie.title = title
                movie.subtitle = subtitle
                movie.description = description
                movie.author = author
                movie.release = datetime.strptime(release, '%Y-%m-%d')
                movie.image = new_image
                db.session.commit()
            except ValueError as e:
                db.session.rollback()
                error = { 'movie_update_value_error' : f'A value error occured. {e}' }
            except IntegrityError as e:
                db.session.rollback()
                error = { 'movie_update_integrity_error' : f"A integrity error occured. {e.code}" }
            else:
                return redirect(url_for('movie.index'))
            
            if error is not None:
                flash(error)

    return render_template('movie/update.html', movie=movie)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    movie = db.get_or_404(Movie, id)
    delete_old_file(movie.image)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('movie.index'))

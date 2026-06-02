from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from datetime import datetime
from flask_login import login_required

bp = Blueprint('moviedb', __name__)

@bp.route('/')
def index():
    movies = [{'Title':'Death Proof', 'Subtitle': 'Tot sicher', 'Author': 'Quentin Tarantino', 'Release': '2008', 'Description': 
               """
                Death Proof is a 2007 American slasher film[2] written, co-produced, shot and directed by Quentin Tarantino. It stars Kurt Russell as a stuntman who murders young women with modified cars he describes as "death-proof". Rosario Dawson, Vanessa Ferlito, Jordan Ladd, Rose McGowan, Sydney Tamiia Poitier, Tracie Thoms, Mary Elizabeth Winstead, and Zoë Bell co-star as the women he targets.
               """,  }]
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

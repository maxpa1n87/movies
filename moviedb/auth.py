import functools

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from moviedb.user import User
from moviedb.database import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                user = User(
                    username=username, 
                    password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
            except Exception:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    pass

@bp.route('/logout')
def logout():
    pass

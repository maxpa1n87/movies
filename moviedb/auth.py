from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from moviedb.shared.models import db
from moviedb.users.models import User
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = { 'auth_register_invalid_username': 'Username is required.' }
        elif not password:
            error = { 'auth_register_invalid_password': 'Password is required.' }

        if error is None:
            try:
                user = User(
                    username=username, 
                    password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                error = { 'auth_register_username_already_registered' : f"User {username} is already registered." }
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = db.session.execute(db.select(User).where(User.username==username)).scalar()

        if user is None:
            error = { 'auth_login_incorrect_username' : 'Incorrect username.' }
        elif not check_password_hash(user.password, password):
            error = { 'auth_login_incorrect_password' : 'Incorrect password.' }

        if error is None:
            login_user(user)
            return redirect(url_for('movie.index'))

        if error is not None:
            flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('movie.index'))

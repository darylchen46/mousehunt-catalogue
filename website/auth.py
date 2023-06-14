from flask import Blueprint, render_template, request, redirect, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        # Check if username field is filled
        if not username:
            flash("Please enter username", category='error')

        elif user:
            if not password:
                flash('Please enter password', category='error')
            elif check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully!", category='success')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")

        user = User.query.filter_by(username=username).first()

        # Check if username exists
        if user:
            flash('Username already exist!', category='error')

        # Check if username field is filled
        elif not username:
            flash("Please enter a username", category='error')

        # Check if length of username is sufficient
        elif len(username) < 3:
            flash("Username needs to be more than 3 characters long", category='error')
        
        # Check if password field is filled
        elif not password:
            flash("Please enter a password. password needs to be more than 8 characters long", category='error')

        # Check if password length is sufficient
        elif len(password) < 8:
            flash("Passwords needs to be more than 8 characters long", category='error')
        
        # Check if confirm password field is filled
        elif not cpassword:
            flash("Please confirm your password", category='error')

        # Check if passwords match
        elif password != cpassword:
            flash("Passwords do not match", category='error')
        
        # Success
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account registered!", category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)
# This file will store all the authentication that users will encounter like login
# The Blueprint will define all the views in one place
# The render template will call-out the respective web page
# The request will enable the requested data to be retrieved from the forms
# The flash will flash a message to the user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Define the login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Verify details from the database
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password! Try again...', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)

# Define the logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Define the sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Get the data submitted in the form
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Set checkpoints of the above
        # Check that the email does not already exist
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            # Add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('New account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
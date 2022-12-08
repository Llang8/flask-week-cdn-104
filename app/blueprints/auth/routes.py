from . import bp as app
from app.blueprints.blog.models import User
from app import db
from flask import redirect, url_for, render_template, request
from flask_login import login_user, logout_user

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # If it gets to this point in the function, 
    # it's a post request
    email = request.form['email']
    password = request.form['password']
    
    user = User.query.filter_by(email=email).first()

    # If user doesn't exist
    if user is None:
        return f'User with email {email} does not exist.'
    elif user.password == password:
        login_user(user)
        return redirect(url_for('main.home'))
    else:
        # The user exists, but the password is wrong
        return 'Password incorrect.'

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    # Otherwise user is making a post request
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    first_name = request.form['firstName']
    last_name = request.form['lastName']

    check_user = User.query.filter_by(email=email).first()

    if check_user is not None:
        return f'User with email {email} already exists.'

    elif password != confirm_password:
        return 'Passwords do not match.'

    else:
        # User can be created
        try:
            new_user = User(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except:
            return 'There was an error.'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
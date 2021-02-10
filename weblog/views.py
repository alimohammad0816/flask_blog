from flask import render_template, url_for, flash, redirect, request
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from .application import app, db, bcrypt
from .models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


blog_posts = [
    {
        "author": "Jan doe",
        "title": "Post1",
        "content": "First post in blog",
        "date_posted": datetime.now(),
    },
    {
        "author": "",
        "title": "Post2",
        "content": "Second post in blog",
        "date_posted": datetime.now(),
    },
    {
        "author": "",
        "title": "Post3",
        "content": "Third post in blog",
        "date_posted": datetime.now(),
    },
    {
        "author": "",
        "title": "Post4",
        "content": "4th post in blog",
        "date_posted": datetime.now(),
    },
]


@app.route("/")
def home():
    posts = blog_posts
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been Created! now able to to login.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(form.email.data)
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("email or password is incorrect!", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

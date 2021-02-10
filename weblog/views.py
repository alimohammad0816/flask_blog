from flask import render_template, url_for, flash, redirect
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from .application import app, db, bcrypt
from .models import User, Post

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
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.password.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been Created! now able to to login.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '12345678':
            flash("Loged In Successfuly!", 'success')
            return redirect(url_for('home'))
        else:
            flash("email or password is incorrect!", 'danger')
    return render_template('login.html', title='Login', form=form)